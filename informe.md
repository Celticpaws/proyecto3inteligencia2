---
graphics: yes
---

\newpage

# Introducción

K-means es un método de agrupamiento, que tiene como objetivo la
partición de un conjunto de n observaciones en k grupos en el que cada
observación pertenece al grupo cuyo valor medio es más cercano. Es un
método muy utilizado en minería de datos debido a su capacidad de
ubicar patrones dentro de un espacio definido de observaciones.

En el siguiente informe se presenta una aplicación del algoritmo
k-means y su representacion grafica en el conjunto de datos "Iris Data
Set" el cual cataloga 3 categorizaciones de una planta de Iris, el
objetivo es que el algoritmo pueda generar la definición de a que
conjunto pertenece una observacion en base a longuitud y ancho del
sepalò y petalo de la flor, para categorizar a que especie pertenece.

\newpage

# Implementación

## Librerias y Funciones Externas Usadas

* *PIL - Image* : Generador de Imagenes jpg
* *Math - random* : Generador de valores pseudo-aleatorios
* *os* : Creador de directorios para el guardado de los graficos generados
* *numpy* : Control de estructuras en el algoritmo k-means
* *matplotlib - pyplot* : Generador de Scatterplots de los conjuntos

## Algoritmo K-means

Para la implementacion del algoritmo k-means se creo el modulo
*k-means.py* el cual contiene las siguientes funciones definidas:
* *puntos_del_cluster*: Clasifica los puntos segun el centroide más
cercano a la observacion

* *centrar*: Calcula el punto medio de las observaciones clasificadas

* *iteracion*: Realiza una iteracion de la clasificacion de los puntos
siempre que el cambio en el centroide varie.

## Programa principal

El archivo principal esta ubicado como *main.py* y el cual lee los
datos del archivo principal *bezdekIris.data* realiza una iteracion
continua centrando los datos y definiendo los nuevos centroides del
conjunto en base a un k definido en la funcion, las iteraciones
continuan formalmente hasta lograr una convergencia, una vez realizada
la convergencia se comprime la informacion en un Scatter plot donde se
toman 2 de las variables para presentar la información (longuitud y
ancho del sepalo) ademas genera una imagen comprimida de los
resultados de cada uno de las observaciones, ambos graficos son
guardados en las carpetas "/Ejercicio_a" o "/Ejercicio_b"
respectivamente dependiendo del enunciado.

\newpage

# Presentación de los resultados

Para la presentacion de los resultados se escogieron las mejores
corridas del algoritmo en base a k a fin de poder presentar la
información mas veraz del mismo.

## Ejercicio a

* k = 2

\begin{center}
\includegraphics[height=4cm]{Ejercicio_a/k_scatter_2.png}
\includegraphics[height=4cm]{Ejercicio_a/Imagen_K2.jpg}
\end{center}

* k = 3

\begin{center}
\includegraphics[height=4cm]{Ejercicio_a/k_scatter_3.png}
\includegraphics[height=4cm]{Ejercicio_a/Imagen_K3.jpg}
\end{center}

* k = 4

\begin{center}
\includegraphics[height=4cm]{Ejercicio_a/k_scatter_4.png}
\includegraphics[height=4cm]{Ejercicio_a/Imagen_K4.jpg}
\end{center}

* k = 5

\begin{center}
\includegraphics[height=4cm]{Ejercicio_a/k_scatter_5.png}
\includegraphics[height=4cm]{Ejercicio_a/Imagen_K5.jpg}
\end{center}

Se puede apreciar que para las corridas con k = {2,3} el algoritmo
puede clasificar con un alto grado de eficiencia el cluster al cual
pertenece cada observación.

* k = 2
Para el caso de k = 2 el algoritmo genera un solo cluster que contiene
2 clasificaciones en conjunto a pesar de ello usalmente entre 3 a 5 de
las 150 observaciones es catalogado de manera incorrecta teniendo en
cuenta que el conjunto "Iris versicolor" e "Iris virginia" pertenecen
al mismo cluster. Generando asi un margen de error de 2% a 3% en la
clasificaciòn

* k = 3
Para el caso de k = 3 el algoritmo genera un solo cluster que contiene
2 clasificaciones en conjunto a pesar de ello usalmente entre 10 a 16
de las 150 observaciones es catalogado de manera incorrecta teniendo
en cuenta que el conjunto "Iris setosa" es catalogado perfectamente en
el 100% de los casos pero debido a la similitud de las observaciones
de "Iris versicolor" e "Iris virginia" el algoritmo tiende a
categorizarlas de manera erronea, se deben realizar multiples corridas
del algoritmo para poder tener en cuenta cual realmente es la
clasificacion de los ultimos 2 conjuntos. Generando asi un margen de
error de 6% a 10% en la clasificaciòn.

## Ejercicio b

Originalmente el conjunto a estudiar se puede presentar en una imagen
comprimida. En este caso cada pixel en la imagen
original es un ejemplo, que será asignado en la imagen comprimida al
cluster ki . K será el número de
colores en la imagen comprimida. Formalmente la imagen original
deberia ser de la siguiente forma:

\begin{center}
\includegraphics[height=6cm]{Imagen_Original.jpg}
\end{center}

Se evalua el algoritmo para los siguientes conjuntos:

* k = 2
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K2.jpg}
\end{center}

* k = 4
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K4.jpg}
\end{center}

* k = 8
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K8.jpg}
\end{center}

* k = 16
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K16.jpg}
\end{center}

* k = 32
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K32.jpg}
\end{center}

* k = 64
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K64.jpg}
\end{center}

* k = 128
\begin{center}
\includegraphics[height=6cm]{Ejercicio_b/Imagen_K128.jpg}
\end{center}

\newpage

# Conclusiones
