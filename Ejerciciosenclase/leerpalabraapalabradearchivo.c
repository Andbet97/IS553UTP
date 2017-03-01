/*lee palabra por palabra de un archivo*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cursor = 0;

struct cadena{
  char palabra[20];
  int evaluador;
};

struct cadena palabra (char *ruta)
{
  struct cadena P;
  P.evaluador = 0;
  int i;
  for (i = 0; i < 20; i++){
    P.palabra[i] = '\0';
  }
  char caracter;
  FILE *archivo;
  archivo = fopen(ruta,"r");
  if (archivo == NULL)
    return P;
  i = 0;
  fseek(archivo, cursor, SEEK_SET);
  while (feof(archivo) == 0){
    caracter = fgetc(archivo);
    cursor++;
    if ((caracter == ' ') || (caracter == '\n'))
      break;
    P.palabra[i] = caracter;
    i++;
    if (feof(archivo))
      P.evaluador = 1;
  }
  fclose (archivo);
  return P;
}

int main()
{
  struct cadena L;
  L.evaluador = 0;
  while (0 == 0){
    L = palabra("prueba.txt");
    if (L.evaluador == 1)
      break;
    printf("%s, longitid: %d\n", L.palabra, strlen(L.palabra));
  }
	return 0;
}
