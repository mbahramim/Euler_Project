N = 100

sum_of_square = 0
for i in range (1 , N + 1):
    sum_of_square = sum_of_square + i * i
print (sum_of_square)

square_of_sum = (N * (N + 1) / 2) * (N * (N + 1) / 2)
print (square_of_sum)
print (square_of_sum - sum_of_square)