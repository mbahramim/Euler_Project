N = 10001

import math

def isprime (x):
    result = True
    for cont in range (2, int (math.sqrt (x)) + 1):
        if x % cont == 0:
            result = False
            break
    return result

i = 1
n_prime = 0

while True:
    i = i + 1
    if isprime (i):
        n_prime = n_prime + 1
        if n_prime == N:
            break

print (i)