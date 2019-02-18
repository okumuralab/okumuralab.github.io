/*********************************************************************
  dumpwave.c

  Usage: dumpwave filename.wav
           or specify number of samples to output, e.g.,
         dumpwave -100 filename.wav (outputs 100 samples)
*********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

long samples_to_output = -1;

unsigned char *get_bytes(FILE *f, int n)
{
    static unsigned char s[16];

    assert (n <= sizeof s);
    if (fread(s, n, 1, f) != 1) {
        fprintf(stderr, "Read error\n");
        exit(1);
    }
    return s;
}

unsigned long get_ulong(FILE *f)
{
    unsigned char *s = get_bytes(f, 4);
    return s[0] + 256LU * (s[1] + 256LU * (s[2] + 256LU * s[3]));
}

unsigned get_ushort(FILE *f)
{
    unsigned char *s = get_bytes(f, 2);
    return s[0] + 256U * s[1];
}

void dumpwave(FILE *f)
{
    int i, x, channels, bits;
    unsigned long len;
    long count;
    unsigned char s[5];
    volatile int v32;
    volatile short v16;

    if (memcmp(get_bytes(f, 4), "RIFF", 4) != 0) {
        fprintf(stderr, "Not a 'RIFF' format\n");
        return;
    }
    fprintf(stderr, "[RIFF] (%lu bytes)\n", get_ulong(f));
    if (memcmp(get_bytes(f, 8), "WAVEfmt ", 8) != 0) {
        fprintf(stderr, "Not a 'WAVEfmt ' format\n");
        return;
    }
    len = get_ulong(f);
    fprintf(stderr, "[WAVEfmt ] (%lu bytes)\n", len);
    fprintf(stderr, "  Data type = %u (1 = PCM)\n", get_ushort(f));
    channels = get_ushort(f);
    fprintf(stderr, "  Number of channels = %u (1 = mono, 2 = stereo)\n", channels);
    fprintf(stderr, "  Sampling rate = %luHz\n", get_ulong(f));
    fprintf(stderr, "  Bytes / second = %lu\n", get_ulong(f));
    fprintf(stderr, "  Bytes x channels = %u\n", get_ushort(f));
    bits = get_ushort(f);
    fprintf(stderr, "  Bits / sample = %u\n", bits);
    for (i = 16; i < len; i++)
        fprintf(stderr, "%02x ", fgetc(f));
    fprintf(stderr, "\n");
    while (fread(s, 4, 1, f) == 1) {
        len = get_ulong(f);
        s[4] = 0;
        fprintf(stderr, "[%s] (%lu bytes)\n", s, len);
        if (memcmp(s, "data", 4) == 0) break;
        for (i = 0; i < len; i++)
            fprintf(stderr, "%02x ", fgetc(f));
        fprintf(stderr, "\n");
    }
    for (count = 0; count != samples_to_output; count++) {
        for (i = 0; i < channels; i++) {
            if (bits <= 8) {
                if ((x = fgetc(f)) == EOF) return;
                x -= 128;
            } else if (bits <= 16) {
                if (fread(s, 2, 1, f) != 1) return;
                v16 = (short)(s[0] + 256 * s[1]);
                x = v16;
            } else if (bits <= 24) {
                if (fread(s, 3, 1, f) != 1) return;
                v32 = (int)(256 * (s[0] + 256 * (s[1] + 256 * s[2])));
                x = v32 / 256;
            } else if (bits <= 32) {
                if (fread(s, 4, 1, f) != 1) return;
                v32 = (int)(s[0] + 256 * (s[1] + 256 * (s[2] + 256 * s[3])));
                x = v32;
            } else {
                fprintf(stderr, "Unsupported: %d bits\n", bits);
            }
            printf("%d", x);
            if (i != channels - 1) printf("\t");
        }
        printf("\n");
    }
}

int main(int argc, char *argv[])
{
    int i;
    FILE *f;

    assert(sizeof(short) == 2);
    assert(sizeof(int) == 4);
    for (i = 1; i < argc; i++) {
        if (argv[i][0] == '-') {
            samples_to_output = atol(&argv[i][1]);
        } else if ((f = fopen(argv[i], "rb")) != NULL) {
            dumpwave(f);  fclose(f);
        } else {
            fprintf(stderr, "Can't open %s\n", argv[i]);
        }
    }
    return 0;
}
