Problema de las N Reinas
Programción IV
Taller N° 1

Andrés Felipe Btancurt Rivera
108802891
andbet050197gmail.com

Fecha de entrega: 14 Febrero 2017
Profesor Ángel Augusto Agudelo Zapata

Enunciado Taller N° 1

Analizar, diseñar e implementar el problema de las 8 reinas en el lenguaje
de su preferencia.
Restricciones:
1)El tamaño del tablero es variable.
2)Debe tomar tiemos ara aber lo que se demora el algoritmo selecionado.
3)Debe motrar el resultado en pantalla.
4)Debe generar una anmación.

Análisis del problema

Este problema consiste, en cortas palabras, en ubicar un numero N de reinas
en un talero de NxN de modo que ninguna de las reinas ataque a otra en el
tablero. Se debe tener en cuenta que las reinas en el juego de ajedrez pueden
moverse en línea recta por las filas, columnas y diagonales.

Solución del problema

El entorno de programación que utilizare sera CodeBlocks.

Para la solución de este problema utilizare el lenguaje C, debido a que hasta
el momento es el único lenguaje que manejo.
Al inicio de la clase cuando se dej el ejercicio tome la decicion de trabajar
con pilas y colas, pensando que podria utiizarla para guardar las poiciones
en la que iba ubicando las reinas. Posteriormente y tras la sugerencia del
profsor y la lectura del articulo de Niklaus Wirth, decido utilizar un único
vector para dar solución al problema.

Puesto que el lenguaje C no posee funciones arraigada que trabajen permutaciones
decidi trabajar la solucón por fuerza bruta o Backtracking.

Aunque ya tenia la solución con Backtracking decido investigar y encuento una
función que genera permutaciones en lenguaje C (la fuente de dicha página se
encuentra en el código de permutacones), por lo tanto en este taller envio
dos solucones.

Para la toma de tiempo utilizare la libreria time.h.

El apartado gráfico es sin duda lo que más dificutades me presenta y es por esto
que decido hacer la animación imrimiendo en pantalla el tablro de ajedrez con
los cambios que se han ido realizando en el código.

Conclusión

Las soluciones de este problema presentan tiempos diferentes, las permutaciones
dan un menor tiempo si N es menor 10 puesto que existen menos permutaciones
sin embargo cuando aumentamos N las permutaciones poibles tardan más tiempo en
realizarse, por lo tanto el Backtracking es más efectivo en valores de N mayores
que 10.
