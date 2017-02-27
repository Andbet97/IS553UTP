#include <stdlib.h>
#include <stdio.h>
#include <string.h>
//  #include <.h>

char Vector[4][6] = {"-help", "-h", "-w", "-file"};
/*    Vector            0       1     2      3*/

int cursor = 0;

struct cadena{
  char palabra[20];
  int evaluador;
};

struct lista{
  int key;
  struct lista *next;
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

void help ()
{
  printf("-help                :Mostrar menu de ayuda.\n");
  printf("-h <valor>           :Modificar el valor de Xmaximo a <valor>.\n");
  printf("-w <valor>           :Modificar el valor de Ymaximo a <valor>.\n");
  printf("-file <file.txt>     :Dar la ruta o el nombre del archivo de valores en <file.tx>.\n");
  return;
}

int verificarlista (char *arg)
{
  int r = 0, i;
  for (i = 1; i < 4; i++){
    if (strcmp(Vector[i], arg) == 0)
      r = i;
  }
  return r;
}

int escalado (int evaluar, int rmn, int rmx, int max)
{
  int pos = 0, cantidad;
  if (rmn < 0){
    max = max*2;
    cantidad = rmx*2;
  }
  else{
    cantidad = rmx - rmn;
  }
  double factor;
  factor = cantidad/max;
  double delta;
  delta = max - (rmx/factor);
  double aux = (evaluar/factor) + delta;
  pos = (int)aux;
  return pos;
}

int main(int argc, char *argv[])
{
  /*Inicio de la lectura de los argumentos*/
  int xmax = 0, ymax = 0;
  char *Archivo = NULL;
  if (argc == 1){
    printf("Error, no se ha detectado el nombre del archivo.\n");
    printf("Intente \"%s -file <file.txt>\"", argv[0]);
    printf(" o \"%s -help\".\n", argv[0]);
    return 1;
  }
  if ((argc == 2) && (strcmp(argv[1], Vector[0]) == 0)){
    help ();
    return 2;
  }
  if ((argc == 2) && (strcmp(argv[1], Vector[0]) != 0)){
    if (verificarlista(argv[1]) != 0){
      printf("El argumento \"%s\" necesita un valor.\n", argv[1]);
      printf("Intente \"%s -help\"\n", argv[0]);
      return 2;
    }
    else{
      printf("El argumento \"%s\" no se reconoce como valido.\n", argv[1]);
      printf("Intente \"%s -help\"\n", argv[0]);
      return 2;
    }
  }
  if ((argc == 3) && (strcmp(argv[1], Vector[3]) == 0) && (verificarlista(argv[2]) == 0)){
    xmax = 80;
    ymax = 23;
    Archivo = argv[2];
  }
  if ((argc == 3) && (xmax == 0)) {
    if (strcmp(argv[1], Vector[3]) == 0){
      printf("El argumento \"-file\" requiere un archivo de entrada.\n");
      printf("Intente \"%s -file <file.txt>\"", argv[0]);
      printf(" o \"%s -help\".\n", argv[0]);
      return 3;
    }
    if (verificarlista(argv[2]) == 0){
      printf("Error, no se ha detectado el nombre del archivo.\n");
      printf("Intente \"%s -file <file.txt>\"", argv[0]);
      printf(" o \"%s -help\".\n", argv[0]);
      return 3;
    }
  }
  if (argc >= 3){
    int i;
    for (i = 1; i < argc; i++){
      if (i+1 >= argc){
        printf("Error, el argumento \"%s\" necesitaun argumento valido.\n", argv[i]);
        printf("Intente \"%s -help\".\n", argv[0]);
        return 4;
      }
      if ((verificarlista(argv[i]) != 0) && (verificarlista(argv[i+1]) == 0)){
        if (verificarlista(argv[i]) == 1){
          if (xmax == 0)
            xmax = atoi(argv[i+1]);
          else{
            printf("Error, el argumento \"-h\" ya se habia utilizado.\n");
            printf("Intente \"%s -help\".\n", argv[0]);
            return 4;
          }
        }
        if (verificarlista(argv[i]) == 2){
          if (ymax == 0)
            ymax = atoi(argv[i+1]);
          else{
            printf("Error, el argumento \"-w\" ya se habia utilizado.\n");
            printf("Intente \"%s -help\".\n", argv[0]);
            return 4;
          }
        }
        if ((verificarlista(argv[i]) == 3) && (argc > 3)){
          if (Archivo == NULL)
            Archivo = argv[i+1];
          else{
            printf("Error, el argumento \"-file\" ya se habia utilizado.\n");
            printf("Intente \"%s -help\".\n", argv[0]);
            return 4;
          }
        }
      }
      if (verificarlista(argv[i]) == 0){
        printf("\"%s\" no se reconoce como argumento.\n", argv[i]);
        printf("Intente \"%s -help\".\n", argv[0]);
        return 4;
      }
      if (verificarlista(argv[i+1]) != 0){
        printf("el argumento \"%s\" requiere un valor valido.\n", argv[i]);
        printf("Intente \"%s -help\".\n", argv[0]);
        return 4;
      }
      i++;
    }
  }
  if (Archivo == NULL){
    printf("Error, no se ha detectado el nombre del archivo.\n");
    printf("Intente \"%s -file <file.txt>\"", argv[0]);
    printf(" o \"%s -help\".\n", argv[0]);
    return 5;
  }
  if (xmax == 0)
    xmax = 80;
  if (ymax == 0)
    ymax = 23;
  fflush(stdin);
  fflush(stdout);
/*Inicio de la lectura de los datos*/
  int desdex, hastax, desdey, hastay = 0, cerox, ceroy;
  struct lista *A[2*ymax+1];
  char titulo[15][20];
  int left_ticks[ymax];
  int bottom_ticks[xmax];
  int i, xmx = 0, xmn = 0, ymx = 0, ymn = 0, palt = 0, left = 0, bottom = 0;
  for (i = 0; i < 15; i++){
    for (xmn = 0; xmn < 20; xmn++){
      titulo[i][xmn] = '\0';
    }
  }
  for (i = 0; i < xmax; i++){
    bottom_ticks[i] = 0;
  }
  for (i = 0; i < ymax; i++){
    left_ticks[i] = 0;
  }
  for (i = 0; i < 2*ymax+1; i++){
    A[i] = NULL;
  }
  xmn = 0;
  struct cadena L;
  L.evaluador = 0;
  while (0 == 0){
    L = palabra(Archivo);
    if (L.evaluador == 1)
      break;
    if (strcmp(L.palabra, "label") == 0){
      L = palabra(Archivo);
      while (strlen(L.palabra) != 0){
        strcpy(titulo[palt], L.palabra);
        palt++;
        L = palabra(Archivo);
      }
    }
    if (strcmp(L.palabra, "range") == 0){
      int c;
      L = palabra(Archivo);
      for (c = 1; c <= 4; c++){
        int n = atoi(L.palabra);
        if (c == 1)
          xmn = n;
        if (c == 2)
          xmx = n;
        if (c == 3)
          ymn = n;
        if (c == 4)
          ymx = n;
        L = palabra(Archivo);
      }
      L = palabra(Archivo);
    }
    if (strcmp(L.palabra, "left") == 0){
      L = palabra(Archivo);
      L = palabra(Archivo);
      while (strlen(L.palabra) != 0){
        int n =  atoi(L.palabra);
        left_ticks[left] = n;
        left++;
        L = palabra(Archivo);
      }
    }
    if (strcmp(L.palabra, "bottom") == 0){
      L = palabra(Archivo);
      L = palabra(Archivo);
      while (strlen(L.palabra) != 0){
        int n =  atoi(L.palabra);
        bottom_ticks[bottom] = n;
        bottom++;
        L = palabra(Archivo);
      }
    }
    if ((L.palabra[1] >= 48) && (L.palabra[1] < 58)){
      int cont = 0;
      int x, y, r;
      while (strlen(L.palabra) != 0){
        if (cont == 0){
          r = atoi(L.palabra);
          x = escalado(r, xmn, xmx, xmax);
        }
        if (cont == 1){
          r = atoi(L.palabra);
          y = escalado(r, ymn, ymx, ymax);
        }
        cont++;
        L = palabra(Archivo);
      }
      if (y < hastay)
        hastay = y;
      struct lista *newnodo;
      newnodo = (struct lista *)malloc(sizeof(struct lista));
      newnodo->key = x;
      newnodo->next = NULL;
      if (A[y] == NULL)
        A[y] = newnodo;
      else{
        newnodo->next = A[y];
        A[y] = newnodo;
      }
    }
  }
  fflush(stdin);
  fflush(stdout);
  /*finaliza la lectura del archivo*/
  desdex = escalado(xmn, xmn, xmx, xmax);
  hastax = escalado(xmx, xmn, xmx, xmax);
  cerox = escalado(0, xmn, xmx, xmax);
  if (cerox < 0)
    cerox = desdex;
  desdey = escalado(ymx, ymn, ymx, ymax);
  ceroy = escalado(0, ymn, ymx, ymax);
  if (ceroy < 0)
    ceroy = hastay;
  system ("cls");
  printf("Titulo\n\n");
  for (i = 0; i < palt; i++){
    printf("%s ", titulo[i]);
  }
  printf("\n\n");
  for (i = desdey; i >= hastay; i--){
    int a, u;
    printf("\t");
    for (a = desdex; a <= hastax; a++){
      u = 0;
      struct lista *q;
      q = A[i];
      int evaluador = 0;
      while(q != NULL){
        if (q->key == a)
          evaluador = 1;
        q = q->next;
      }
      if (evaluador == 1){
        printf("*");
      }
      else{
        if (u == 0){
          if (a == cerox){
            printf("%c", 186);
            u = 1;
          }
          if (i == ceroy){
            printf("%c", 205);
            u = 1;
          }
        }
      }
      if ((evaluador == 0) && (u == 0)){
        printf(" ");
        u = 1;
      }
    }
    printf("\n");
    fflush(stdin);
    fflush(stdout);
    free(A[i]);
  }
  struct lista *p;
  p = A[10];
  while(p != NULL){
    printf("%d, ", p->key);
    p = p->next;
  }
  return 0;
}
