def factorial(x):
    if x == 0: return 1
    return x * factorial(x - 1)

max_i = 50
n = range(1, max_i + 1)
for i in n:
    print('The value of ' + str(i) + '! is ' + str(factorial(i)) + '.')
