/*Taller N°1 Solución por medio de Backtracking
Andrés Felipe Btncurt Rivera 108808961 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int evaluar (int V[], int p, int n)
{/*arregar*/
  int r = 0;
  int x, y;
  int i;
  if (p == 1)
    return r;
  for (i = 1; i < p; i++){
    if (V[i] == V[p]){
      r = 1;
      break;
    }
    if (V[i] > V[p])
      y = V[i] - V[p];
    else
      y = V[p] - V[i];
    x = p - i;
    if (x == y){
      r = 1;
      break;
    }
  }
  return r;
}

void mostrar_tablero (int V[], int n)
{
  int i = 1, x = 1;
  while (i <= n){
    if (V[x] == i)
      printf("%c ", 'Q');
    else
      printf("%c ", 254);
    x++;
    if (x > n){
      printf("\n");
      x = 1;
      i++;
    }
  }
}

int main ()
{
  time_t inicio, fin;
  double tiempo;
  int n;
  int a, p, i, e;
  printf ("ingrese el valor de n: ");
  scanf("%d", &n);
  inicio = time(NULL);
  int V[n+1];
  for (i = 1; i <= n; i++){
    V[i] = 0;
  }
  a = 1;
  while ((a > 0)&&(a <= n)){
    V[a] = V[a]+1;
    if (V[a] > n){
      V[a] = 0;
      a--;
    }
    else {
      e = evaluar (V, a, n);
      if (e == 0)
        a++;
      if ((V[a] == n)&&(e == 1)){
        V[a] = 0;
        a--;
      }
    }
    system ("cls");
    mostrar_tablero (V, n);
    for (i = 0; i < 30000; i++){
      for (p = 0; p < 10000; p++){
      }
    }
  }
  system ("cls");
  mostrar_tablero (V, n);
  printf("\nVector: ");
  for (i = 1; i <= n; i++){
    printf("%d ", V[i]);
  }
  fin = time(NULL);
  tiempo = difftime(fin, inicio);
  printf("\nTiempo total: %g segundos\n", tiempo);
  return 0;
}
