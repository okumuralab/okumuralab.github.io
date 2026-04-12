#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


PATTERN = re.compile(
    r"""
    \{
        "date"\s*:\s*"(?P<date>\d{4}-\d{2}-\d{2})"\s*,
        "timestamp"\s*:\s*(?P<timestamp>\d+)\s*,
        "followee"\s*:\s*(?P<followee>\d+)\s*,
        "follower"\s*:\s*(?P<follower>\d+)\s*,
        "statuses"\s*:\s*(?P<statuses>\d+)
    \}
    """,
    re.VERBOSE,
)

FIELDNAMES = ["date", "timestamp", "followee", "follower", "statuses"]


def extract_rows(html_text: str) -> list[dict[str, int | str]]:
    rows: list[dict[str, int | str]] = []
    for match in PATTERN.finditer(html_text):
        rows.append(
            {
                "date": match.group("date"),
                "timestamp": int(match.group("timestamp")),
                "followee": int(match.group("followee")),
                "follower": int(match.group("follower")),
                "statuses": int(match.group("statuses")),
            }
        )
    return rows


def write_csv(rows: list[dict[str, int | str]], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract date/timestamp/followee/follower/statuses records from stats.html into CSV."
    )
    parser.add_argument(
        "input_html",
        nargs="?",
        default="stats.html",
        help="Path to the source HTML file. Default: stats.html",
    )
    parser.add_argument(
        "output_csv",
        nargs="?",
        default="stats.csv",
        help="Path to the output CSV file. Default: stats.csv",
    )
    args = parser.parse_args()

    input_path = Path(args.input_html)
    output_path = Path(args.output_csv)

    html_text = input_path.read_text(encoding="utf-8")
    rows = extract_rows(html_text)

    if not rows:
        raise SystemExit("No matching records were found.")

    write_csv(rows, output_path)
    print(f"Wrote {len(rows)} rows to {output_path}")


if __name__ == "__main__":
    main()
