#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define RAND_MAX ((1U << 31) - 1)
#define MAXLENGTH 80

int realrand() {
	int n;
	FILE *fp = fopen("/dev/urandom", "r");
	fread(&n, 4, 1, fp);
	fclose(fp);
	return n % MAXLENGTH;
}

int seed;

int pseudorand() {
	return seed = (seed * 19394489 + 132241) & 0xff;
}

int main() {
	char input[MAXLENGTH];
	FILE *fp = fopen("flag.in", "r");
	fread(&input, 1, MAXLENGTH, fp);
	fclose(fp);

	fp = fopen("flag.out", "wb");
	seed = realrand();
	int r;
	char c;
	for (int i = 0, l = strlen(input); i < l; ++i) {
		c = ((char) input[i] ^ (r = pseudorand())) & 0xff;
		fwrite(&c, 1, 1, fp);
	}
	fclose(fp);
}
