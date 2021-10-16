#!/usr/bin/python3
#<class 'list'> 

# 2021/10/16 PSR
# BP
# Programa que devolve os numeros perfeitos até um determinado máximo   maximum_number

maximum_number = 100

#
# Função isPerfect - devolve true ou false caso o numero seja perfeito ou nao
#

thislist = []

def isPerfect(value):
    # <Fill the blanks>
    # soma dos divisores igualam o número) como por exemplo 6 = 3 + 2 + 1
    soma = 0
    thislist.clear()
    #print('Começa o 24 :: ' + str(value) )
    for i in range(1, value):
        remainder = value % i
     #   print('remainder ' + str(remainder) + '     i ' + str(i))
        if remainder == 0:
            thislist.append(i)
            soma = soma + i
    if soma ==  value:
    	return True
    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number): #range(24, 25): #
        if isPerfect(i):
            print(thislist)
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
    
