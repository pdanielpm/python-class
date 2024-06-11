'''
NAME
COUNT-ATCG

VERSION
[1.3]

AUTHOR
Pedro Daniel Pineda Martinez (pedropm@lcg.unam.mx)    

DESCRIPTION
Este programa cuenta el numero de  cada nucleótido (A,T,C,G) en un archivo dado por el usuario que contiene una secuencia de ADN

CATEGORY
Programa que cuenta el numero de nucleótidos en una secuencia de ADN

USAGE

python count_atcg.py archivo.txt --nucleotidos ATCG

python3 count_atcg.py archivo.txt --nucleotidos ATCG

ARGUMENTS

--nucleotidos: Letras de nucleótidos a contar, por defecto cuenta A, T, C, y G

archivo.txt: Nombre del archivo que contiene la secuencia de ADN de la cual se contaran los nucleótidos

METHOD

SEE ALSO

      
'''
# ===========================================================================
# =                            imports
# ===========================================================================
import argparse

# ===========================================================================
# =                            main
# ===========================================================================

# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description='Contar nucleótidos en una secuencia de ADN.')
parser.add_argument('archivo', type=str, help='Nombre del archivo que contiene la secuencia de ADN')
parser.add_argument('--nucleotidos', type=str, default='ATCG', help='Letras de nucleótidos a contar, por defecto cuenta A, T, C, y G')

# Parsear los argumentos de la línea de comandos
args = parser.parse_args()
archivo = args.archivo
nucleotidos_a_contar = args.nucleotidos.upper()


# Variables para contar los nucleótidos
conteos = {nucleotido: 0 for nucleotido in nucleotidos_a_contar}

try:
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leer la secuencia de ADN del archivo
        secuencia = file.read().strip().upper()

        # Verificar si el archivo está vacío
        if not secuencia:
            print("Sorry, the file is empty.")
        else:
             # Verificar si la secuencia contiene caracteres inválidos
            for nucleotido in secuencia:
                if nucleotido not in nucleotidos_a_contar:
                    print(f"Sequence contains [{nucleotido}], it is an invalid character.")
                    break
            else:      
            # Contar los nucleótidos en la secuencia
                for nucleotido in secuencia:
                    if nucleotido in conteos:
                        conteos[nucleotido] += 1

             # Mostrar los resultados
            print("Conteo de nucleótidos:")
            for nucleotido, conteo in conteos.items():
                print(f"{nucleotido}: {conteo}")
except FileNotFoundError:
    print("Sorry, couldn't find the file.")