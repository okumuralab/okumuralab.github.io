#!/usr/bin/env python3
"""
Dump the tokenizer vocabulary embedded in a GGUF model file.

GGUF stores tokenizer vocabulary in metadata, usually under:

    tokenizer.ggml.tokens

This script reads only the GGUF header and metadata section. It does not load
tensor data, so it is suitable even for large model files.
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import json
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Any


GGUF_MAGIC = b"GGUF"

GGUF_UINT8 = 0
GGUF_INT8 = 1
GGUF_UINT16 = 2
GGUF_INT16 = 3
GGUF_UINT32 = 4
GGUF_INT32 = 5
GGUF_FLOAT32 = 6
GGUF_BOOL = 7
GGUF_STRING = 8
GGUF_ARRAY = 9
GGUF_UINT64 = 10
GGUF_INT64 = 11
GGUF_FLOAT64 = 12

TYPE_NAMES = {
    GGUF_UINT8: "uint8",
    GGUF_INT8: "int8",
    GGUF_UINT16: "uint16",
    GGUF_INT16: "int16",
    GGUF_UINT32: "uint32",
    GGUF_INT32: "int32",
    GGUF_FLOAT32: "float32",
    GGUF_BOOL: "bool",
    GGUF_STRING: "string",
    GGUF_ARRAY: "array",
    GGUF_UINT64: "uint64",
    GGUF_INT64: "int64",
    GGUF_FLOAT64: "float64",
}

PRIMITIVE_FORMATS = {
    GGUF_UINT8: "B",
    GGUF_INT8: "b",
    GGUF_UINT16: "H",
    GGUF_INT16: "h",
    GGUF_UINT32: "I",
    GGUF_INT32: "i",
    GGUF_FLOAT32: "f",
    GGUF_BOOL: "?",
    GGUF_UINT64: "Q",
    GGUF_INT64: "q",
    GGUF_FLOAT64: "d",
}


@dataclass(frozen=True)
class GGUFString:
    text: str
    raw: bytes


@dataclass(frozen=True)
class GGUFArray:
    item_type: int
    values: list[Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dump tokenizer vocabulary from a GGUF file."
    )
    parser.add_argument(
        "-m",
        "--model",
        required=True,
        type=Path,
        help="Path to the GGUF model file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output text file. If omitted, writes to standard output.",
    )
    parser.add_argument(
        "--format",
        choices=("plain", "tsv", "jsonl"),
        default="tsv",
        help="Output format. Default: tsv.",
    )
    parser.add_argument(
        "--raw-bytes",
        action="store_true",
        help="For jsonl output, include the GGUF token string's raw bytes as base64.",
    )
    parser.add_argument(
        "--decode",
        choices=("auto", "none", "byte-level"),
        default="auto",
        help=(
            "How to decode token strings for output. "
            "Use byte-level for GPT-2/Qwen byte-level BPE. Default: auto."
        ),
    )
    parser.add_argument(
        "--decode-errors",
        choices=("replace", "ignore", "backslashreplace"),
        default="replace",
        help="UTF-8 error handling used with --decode byte-level. Default: replace.",
    )
    parser.add_argument(
        "--no-escape",
        action="store_true",
        help="Write token text literally instead of escaping tabs/newlines/control characters.",
    )
    parser.add_argument(
        "--list-tokenizer-keys",
        action="store_true",
        help="Print tokenizer-related GGUF metadata keys to stderr.",
    )
    return parser.parse_args()


def read_exact(f: BinaryIO, size: int) -> bytes:
    data = f.read(size)
    if len(data) != size:
        raise EOFError(f"Unexpected end of file while reading {size} bytes")
    return data


def read_u32(f: BinaryIO) -> int:
    return struct.unpack("<I", read_exact(f, 4))[0]


def read_u64(f: BinaryIO) -> int:
    return struct.unpack("<Q", read_exact(f, 8))[0]


def read_primitive(f: BinaryIO, value_type: int) -> Any:
    try:
        fmt = PRIMITIVE_FORMATS[value_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported GGUF value type: {value_type}") from exc
    return struct.unpack("<" + fmt, read_exact(f, struct.calcsize(fmt)))[0]


def read_string(f: BinaryIO) -> GGUFString:
    size = read_u64(f)
    raw = read_exact(f, size)
    return GGUFString(text=raw.decode("utf-8", errors="replace"), raw=raw)


def read_value(f: BinaryIO, value_type: int) -> Any:
    if value_type == GGUF_STRING:
        return read_string(f)
    if value_type == GGUF_ARRAY:
        item_type = read_u32(f)
        item_count = read_u64(f)
        values = [read_value(f, item_type) for _ in range(item_count)]
        return GGUFArray(item_type=item_type, values=values)
    return read_primitive(f, value_type)


def read_metadata(model_path: Path) -> dict[str, Any]:
    with model_path.open("rb") as f:
        magic = read_exact(f, 4)
        if magic != GGUF_MAGIC:
            raise SystemExit(f"Not a GGUF file: {model_path}")

        version = read_u32(f)
        if version < 1:
            raise SystemExit(f"Unsupported GGUF version: {version}")

        _tensor_count = read_u64(f)
        metadata_count = read_u64(f)
        metadata: dict[str, Any] = {}

        for _ in range(metadata_count):
            key = read_string(f).text
            value_type = read_u32(f)
            metadata[key] = read_value(f, value_type)

    return metadata


def require_array(metadata: dict[str, Any], key: str) -> GGUFArray | None:
    value = metadata.get(key)
    if value is None:
        return None
    if not isinstance(value, GGUFArray):
        raise SystemExit(f"Metadata key is not an array: {key}")
    return value


def escape_field(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("\t", "\\t")
        .replace("\r", "\\r")
        .replace("\n", "\\n")
    )


def as_text(value: Any) -> str:
    if isinstance(value, GGUFString):
        return value.text
    return str(value)


def gpt2_byte_decoder() -> dict[str, int]:
    byte_values = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    code_points = byte_values[:]
    next_code_point = 0
    for byte in range(256):
        if byte not in byte_values:
            byte_values.append(byte)
            code_points.append(256 + next_code_point)
            next_code_point += 1
    return {chr(code_point): byte for byte, code_point in zip(byte_values, code_points)}


BYTE_DECODER = gpt2_byte_decoder()


def should_decode_byte_level(args: argparse.Namespace, metadata: dict[str, Any]) -> bool:
    if args.decode == "byte-level":
        return True
    if args.decode == "none":
        return False

    tokenizer_model = metadata.get("tokenizer.ggml.model")
    tokenizer_pre = metadata.get("tokenizer.ggml.pre")
    model_name = as_text(tokenizer_model).lower() if tokenizer_model is not None else ""
    pre_name = as_text(tokenizer_pre).lower() if tokenizer_pre is not None else ""
    return model_name == "gpt2" or pre_name.startswith("qwen")


def decode_byte_level_token(token: GGUFString, errors: str) -> str:
    try:
        token_bytes = bytes(BYTE_DECODER[char] for char in token.text)
    except KeyError:
        return token.text
    return token_bytes.decode("utf-8", errors=errors)


def write_vocab(args: argparse.Namespace, metadata: dict[str, Any]) -> None:
    tokens = require_array(metadata, "tokenizer.ggml.tokens")
    if tokens is None:
        available = ", ".join(k for k in metadata if k.startswith("tokenizer."))
        raise SystemExit(
            "tokenizer.ggml.tokens was not found in GGUF metadata."
            + (f" Available tokenizer keys: {available}" if available else "")
        )
    if tokens.item_type != GGUF_STRING:
        item_name = TYPE_NAMES.get(tokens.item_type, str(tokens.item_type))
        raise SystemExit(f"tokenizer.ggml.tokens has unexpected item type: {item_name}")

    scores = require_array(metadata, "tokenizer.ggml.scores")
    token_types = require_array(metadata, "tokenizer.ggml.token_type")
    decode_byte_level = should_decode_byte_level(args, metadata)

    output_context = (
        args.output.open("w", encoding="utf-8", newline="\n")
        if args.output
        else contextlib.nullcontext(sys.stdout)
    )
    with output_context as output:
        for token_id, token in enumerate(tokens.values):
            if not isinstance(token, GGUFString):
                raise SystemExit(f"Unexpected token entry at id {token_id}")

            decoded_token = (
                decode_byte_level_token(token, args.decode_errors)
                if decode_byte_level
                else token.text
            )
            token_text = decoded_token if args.no_escape else escape_field(decoded_token)
            score = scores.values[token_id] if scores and token_id < len(scores.values) else None
            token_type = (
                token_types.values[token_id]
                if token_types and token_id < len(token_types.values)
                else None
            )

            if args.format == "plain":
                print(token_text, file=output)
            elif args.format == "tsv":
                fields = [str(token_id), token_text]
                if score is not None:
                    fields.append(as_text(score))
                if token_type is not None:
                    fields.append(as_text(token_type))
                print("\t".join(fields), file=output)
            else:
                item = {
                    "id": token_id,
                    "token": decoded_token,
                }
                if decode_byte_level:
                    item["gguf_token"] = token.text
                if score is not None:
                    item["score"] = score
                if token_type is not None:
                    item["type"] = token_type
                if args.raw_bytes:
                    item["raw_bytes_base64"] = base64.b64encode(token.raw).decode("ascii")
                print(json.dumps(item, ensure_ascii=False), file=output)


def main() -> None:
    args = parse_args()
    if not args.model.exists():
        raise SystemExit(f"GGUF file not found: {args.model}")

    metadata = read_metadata(args.model)
    if args.list_tokenizer_keys:
        for key in sorted(k for k in metadata if k.startswith("tokenizer.")):
            value = metadata[key]
            if isinstance(value, GGUFArray):
                type_name = TYPE_NAMES.get(value.item_type, str(value.item_type))
                print(f"{key}: array<{type_name}>[{len(value.values)}]", file=sys.stderr)
            else:
                print(f"{key}: {as_text(value)}", file=sys.stderr)

    write_vocab(args, metadata)


if __name__ == "__main__":
    main()
