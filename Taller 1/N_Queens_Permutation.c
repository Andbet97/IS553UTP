/*Taller N°1 Solución por medio de permutacones
Andrés Felipe Btncurt Rivera 108808961 */
/*FUENTE del código de permutacones: http://rosettacode.org/wiki/Permutations#C_3 (solo uso perm1)*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* next lexicographical permutation */
int next_lex_perm(int *a, int n) {
#	define swap(i, j) {t = a[i]; a[i] = a[j]; a[j] = t;}
	int k, l, t;

	/* 1. Find the largest index k such that a[k] < a[k + 1]. If no such
	      index exists, the permutation is the last permutation.*/
	for (k = n - 1; k && a[k - 1] >= a[k]; k--);
	if (!k--) return 0;

	/* 2. Find the largest index l such that a[k] < a[l]. Since k + 1 is
	   such an index, l is well defined*/
	for (l = n - 1; a[l] <= a[k]; l--);

	/* 3. Swap a[k] with a[l]*/
	swap(k, l);

	/* 4. Reverse the sequence from a[k + 1] to the end*/
	for (k++, l = n - 1; l > k; l--, k++)
		swap(k, l);
	return 1;
#	undef swap
}

int evaluar(int *v, int n)
{
  int i = 1, x = 0, r = 0;
  while (1 == 1){
		if (x == n-1)
			break;
		int a, b;
		if (v[x] > v[i]){
			a = v[x] - v[i];
		}
		else {
			a = v[i] - v[x];
		}
		b = i - x;
		if (a == b){
			r = 1;
			break;
		}
		i++;
		if (i == n){
			x++;
			i = x+1;
		}
	}
  return r;
}

void mostrar_tablero (int V[], int n)
{
  int i = 0, x = 0;
  while (i < n){
    if (V[x] == i+1)
      printf("%c ", 'Q');
    else
      printf("%c ", 254);
    x++;
    if (x == n){
      printf("\n");
      x = 0;
      i++;
    }
  }
}

void perm1(int *x, int n)
{
  int i, p, D[2*n];
  int e;
  while (1 == 1){
    e = evaluar(x, n);
    if (e == 0)
      break;
		system ("cls");
		mostrar_tablero (x, n);
		for (i = 0; i < 30000; i++){
			for (p = 0; p < 10000; p++){
			}
		}
    next_lex_perm(x, n);
  }
}

int main()
{
	time_t inicio, fin;
  double tiempo;
  int n;
  printf("Ingrese el valor de n: ");
  scanf("%d", &n);
	inicio = time(NULL);
  int i, x[n];
	for (i = 0; i < n; i++)
  x[i] = i + 1;
	perm1(x, n);
	system ("cls");
	mostrar_tablero (x, n);
	printf("\n");
	printf("Vector: ");
	for (i = 0; i < n; i++){
		printf("%d ", x[i]);
	}
	fin = time(NULL);
  tiempo = difftime(fin, inicio);
  printf("\nTiempo total: %g segundos\n", tiempo);
	return 0;
}
