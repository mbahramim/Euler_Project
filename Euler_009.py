import math

N = 1000

for a in range (1, N):
    for b in range (a, N):
        c = N - a - b
        a2 = a * a
        b2 = b * b
        c2 = c * c
        if (a2 + b2) == c2:
            print(a)
            print(b)
            print(c)
            print(a * b * c)
            break
