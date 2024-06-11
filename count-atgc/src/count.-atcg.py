'''
NAME
COUNT-ATCG

VERSION
[1.0]

AUTHOR
Pedro Daniel Pineda Martinez (pedropm@lcg.unam.mx)    

DESCRIPTION
Este programa cuenta el numero de  cada nucleótido (A,T,C,G) en una secuencia dada por un archivo llamado sequence.txt  

CATEGORY
Programa que cuenta el numero de nucleótidos en una secuencia de ADN

USAGE

python count_atcg.py

python3 count_atcg.py

ARGUMENTS


METHOD


SEE ALSO

      
'''


# ===========================================================================
# =                            main
# ===========================================================================

# Nombre del archivo que contiene la secuencia de ADN
archivo = 'sequence.txt'

# Variables para contar los nucleótidos
cont_A = 0
cont_T = 0
cont_C = 0
cont_G = 0

# Abrir el archivo en modo lectura
with open(archivo, 'r') as file:
    # Leer la secuencia de ADN del archivo
    secuencia = file.read().strip().upper()

    # Contar los nucleótidos en la secuencia
    for nucleotido in secuencia:
        if nucleotido == 'A':
            cont_A += 1
        elif nucleotido == 'T':
            cont_T += 1
        elif nucleotido == 'C':
            cont_C += 1
        elif nucleotido == 'G':
            cont_G += 1

# Mostrar los resultados
print("Conteo de nucleótidos:")
print(f"A: {cont_A}")
print(f"T: {cont_T}")
print(f"C: {cont_C}")
print(f"G: {cont_G}")
