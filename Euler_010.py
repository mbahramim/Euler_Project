N = 2000000

import math

def isprime (x):
    result = True
    for cont in range (2, int (math.sqrt (x)) + 1):
        if x % cont == 0:
            result = False
            break
    return result

res = 0
for i in range (2, N):
    if isprime (i):
        res = res + i

print (res)