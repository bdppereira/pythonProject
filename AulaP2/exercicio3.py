# 2021/10/21 PSR Aula P2
# BP
# Exercico 2
# Separar o ficheiro primo.py em dois ficheiros distintos.
#
# main.py -> inclui a função principal (main)
# my_functions.py -> contém a função de teste dos números.

import sys

from exercicio2isprime import *


def main():
    for arg in sys.argv[1:]:
        print (arg)

    maximum_number = int(sys.argv[1])
    print("Starting to compute prime numbers up to " + str(maximum_number))

    counter = 0
    for i in range(1, maximum_number):
        if isPrime(i):
            counter = counter + 1
            print( 'Number ' + str(i) + ' is prime.' )
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()
