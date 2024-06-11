# Casos de prueba o escenarios

### Caso de prueba 1: Conteo de todos los nucleotidos en el archivo, no se especifican los nucleotidos.
Comando:
python count_atgc.py archivo.txt

Resultado esperado:

Conteo de nucleótidos:
A: 2
T: 2
C: 2
G: 2

### Caso de prueba 2: Conteo de nucleotidos especificos
Comando:

python count_atgc.py archivo.txt --nucleotidos AC
Resultado esperado:
Conteo de nucleótidos:
A: 2
C: 2


### Caso de prueba 3: Archivo inexistente 
Comando:
python count_atgc.py archivo.txt

Resultado esperado:
Sorry, couldn't find the file.

### Caso 4: Conteo de nucleótidos en un archivo con caracteres no válidos 
Comando:
python count_atgc.py archivo.txt

Resultado esperado:
"Sequence contains [caracter], it is invalid character".

### Caso 5: Conteo de todos los nucleótidos en un archivo con letras minúsculas o mayusculas
Comando:

python count_atgc.py archivo.txt

Conteo de nucleótidos:
A: 3
T: 3
C: 3
G: 1

## Caso 6: Conteo de nucleótidos específicos (A y T) en un archivo con letras minúsculas o mayusculas
Comando:
python count_atgc.py  archivo.txt --nucleotidos AT

Resultado esperado:
Conteo de nucleótidos:
A: 3
T: 3

        