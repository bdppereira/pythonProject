def isPrime(value):
   # print('\nReference number ' + str(value))

    for i in range(2, value):
        remainder = value % i
   #     print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True