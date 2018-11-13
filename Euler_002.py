Max_num = 4000000

sum = 0

first = 1
second = 1

while second < Max_num:
    tmp = first + second
    if tmp % 2 == 0:
        sum = sum + tmp
    first = second
    second = tmp

print(sum)