import math

def isprime (x):
    result = True
    for cont in range (2, int (math.sqrt (x)) + 1):
        if x % cont == 0:
            result = False
            break
    return result

# Num = 13195
Num = 600851475143

cont = 2
while True:
    if Num % cont == 0:
        factor = Num / cont
        if isprime (factor):
            print (factor)
            break
    cont = cont + 1