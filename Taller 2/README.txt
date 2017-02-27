Grficador
Programción IV
Taller N° 2

Andrés Felipe Btancurt Rivera
108802891
andbet050197gmail.com

Fecha de entrega: 24 Febrero 2017
Profesor Ángel Augusto Agudelo Zapata

Análisis del problema

Este programa consiste en recibir un archivo con una serie de parametros que me
determinan tanto la coordenadas como valores extras, ya sea el titulo de la
grafica o los rangos validos para dicha grafica.

Como ejemplo presentare el correo que el profesor compartio por correo:
label Annual Traffic Deaths, USA, 1925-1984  -->En esta inea se presenta el titulo
                                                del grafico.
range 1920 5000 1990 60000                   -->En esta linea se presentan los rangos.
left ticks 10000 30000 50000                 -->En esta linea se presentan las marcas
                                                del eje y.
bottom ticks 1930 1940 1950 1960 1970 1980   -->En esta linea se presentan las marcas
                                                del eje x.
1925 21800                                   -->A partir de aqui se presentan las
1930 31050                                      coordenada
1935 36369
1981 51500
    ...
1982 46000
1983 44600
1984 46200

Ademas de lo anterior el programa debe prmitir a entrada de argumentos, por
ejemplo:

nombre_del_rograma -h x -w y -filenmbre_archivo


Solución del problema

El entorno de programación que utilizare sera CodeBlocks.

Para la solución de este problema utilizare el lenguaje C, debido a que hasta
el momento es el único lenguaje que manejo.

Para la parte de los argumentos he utilizado argc y argv, ademas para l manjo de estos
una serie de condiciones que me aseguran que se manejen de forma correcta.

Para la lectura del archivo utilice las funciones incluidas n la libreria <stdio.h>
y cree una función que me permitiera leer palabra por palabra del archivo.
mientras esto ocurre voy guardando la informacion de mnra que pueda accder a ella
sin necesidad del archivo.

Para guardar las coordenadas decido apoyarme en la explicacion de uno de mis
compañeros e mplementar una funcion de escalamiento que me permite almacnar de una
manera mas comoda las coordenadas.

Para almacenar las coordenadas decido usar un vector de istas ya que es las fácil
recorre la lista. El vector eta ordenado con respecto al eje "y" para facilitar a
la vez su impresion en pantalla.

Para la impresión en pantalla utilizo dos ciclos for que recorreran las listas ya
creadas.

Manera de compilar

La forma que decido implementar es la siguiente:

nombre_del_programa -file nombre_del_archivo.txt

Ej:

Graficador -file prueba.txt

ademas si se digta -help se desplegara un manual de ayuda para mejor comprencón.
