/*FUENTE del código de permutacones: http://rosettacode.org/wiki/Permutations#C_3 (Metodo 1)*/

#include <stdio.h>
#include <stdlib.h>

/* print a list of ints */
int show(int *x, int len)
{
	int i;
	for (i = 0; i < len; i++)
		printf("%d%c", x[i], i == len - 1 ? '\n' : ' ');
	return 1;
}

/* next lexicographical permutation */
int next_lex_perm(int *a, int n) {
#	define swap(i, j) {t = a[i]; a[i] = a[j]; a[j] = t;}
	int k, l, t;

	/* 1. Find the largest index k such that a[k] < a[k + 1]. If no such
	      index exists, the permutation is the last permutation. */
	for (k = n - 1; k && a[k - 1] >= a[k]; k--);
	if (!k--) return 0;

	/* 2. Find the largest index l such that a[k] < a[l]. Since k + 1 is
	   such an index, l is well defined */
	for (l = n - 1; a[l] <= a[k]; l--);

	/* 3. Swap a[k] with a[l] */
	swap(k, l);

	/* 4. Reverse the sequence from a[k + 1] to the end */
	for (k++, l = n - 1; l > k; l--, k++)
		swap(k, l);
	return 1;
#	undef swap
}

void perm1(int *x, int n, int callback(int *, int))
{
	do {
		if (callback) callback(x, n);
    /*aqui se pueden hacer modificaciones*/
	} while (next_lex_perm(x, n));
}



#define N 3

int main()
{
	int i, x[N];
	for (i = 0; i < N; i++) x[i] = i + 1;
	perm1(x, N, show);

	return 0;
}
