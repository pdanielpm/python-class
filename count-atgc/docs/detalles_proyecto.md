#  Count-atcg

**Fecha **: 12/04/24

**Participantes**: Pedro Daniel Pineda Martínez(pedropm@lcg.unam.mx)



## Descripción del Problema

Este programa cuenta el numero de  cada nucleótido (A,T,C,G) en una secuencia dada por un archivo llamado sequence.txt


## Especificación de Requisitos

Requisitos funcionales

* Capacidad de leer cada nucleótido a partir de un archivo 
* Capacidad de calcular el numero de apariciones de cada nucleótido
* Desplegar un mensaje de error si no se encuentra el archivo

Requisitos no funcionales

* Lenguaje de programación(Python)
* Tiempo de calculo y respuesta rápido
* Archivo en un formato especifico


## Análisis y Diseño

Para empezar con el conteo de nucleótidos se necesita leer el archivo, se inicializan los contadores A, T, C y G que se utilizaran para contar la cantidad de cada nucleotido en el archivo dado por el usuario.
Despues se abre el archivo llamado sequence.txt y va recorriendo la cadena de nucleotidos que se encuentra en el archivo, si encuentra cualquiera de las 4 letras se van sumando a las variables.
Se imprime la cantidad de cada nucleotido que se encontro en la cadena.




- **Actor**: Usuario
- **Descripción**: El usuario ingresa el archivo que contiene la secuencia de nucleotidos llamado sequence.txt, el programa calcula la aparicion de cada nucleotido e imprime el resultado.

- **Flujo principal**: 
1. El usuario ingresa el archivo sequence.txt
2. El programa calcula la aparicion de cada nucleotido e imprime el resultado.

- **Flujos alternativos**:
1. Si no se proporciona un archivo, el programa no se ejecuta.
