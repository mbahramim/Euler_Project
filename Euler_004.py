digit_num = 3
ans = 0

def reverse (x):
    x_str = str (x)
    length = len (x_str)
    result = 0
    for i in range (0, length):
        temp = x % 10
        result = result + temp * (10 ** (length - 1 - i))
        x = x - temp
        x = x / 10
    return result

Num_max = 10 ** digit_num - 1
Num_min = 10 ** (digit_num - 1) + 1

for cont1 in xrange (Num_max, Num_max / 2 + 1, -1):
    for cont2 in xrange (cont1, Num_min, -1):
        tmp = cont1 * cont2
        if tmp == reverse (tmp):
            if tmp > ans:
                ans = tmp

print (ans)