N = 20

def dividable_by_each_number (x ,n):
    result = True
    for i in range (2, n + 1):
        result = result and (x % i == 0)
    return result

j = N + 1
while True:
    if dividable_by_each_number (j, N):
        print (j)
        break
    else:
        j = j + 1