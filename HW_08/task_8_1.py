from random import randint


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 2)


fact_list = [randint(1, 10) for i in range(5)]
for i in fact_list:
    print(f'{i}!! = {factorial(i)}')
