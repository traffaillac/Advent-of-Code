#include <stdio.h>

int main() {
	int a = 1, b = 0, c = 0, d = 0, e = 0;
	b = 2 * 2 * 19 * 11 + 4 * 22 + 19; // 943
	if (a) {
		b += (27 * 28 + 29) * 30 * 14 * 32; // 10550400
		a = 0;
	}
	for (int e = 1; e <= b; e++) {
		if (b % e == 0)
			a += e;
	}
	printf("%d\n", a);
	return 0;
}
