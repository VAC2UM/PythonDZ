# пока не работает
import math


def calc(A):
    answ = 1
    for alph in A:
        answ *= alph % 3
    return answ

def main(input_set):
    # вычисляем K
    K = {v for v in input_set if 72 > v > -36}

    # вычисляем B
    B = {abs(v) for v in input_set if -52 < v < 99999999999999999999}

    # вычисляем A
    A = {b ** 3 - math.floor(k / 5) for b in B for k in K if b > k}

    answ = len({(a, b) for a in K for b in A}) + calc(A)

    return answ

ex1 = {89, -31, -93, 69, 74, 46, 80, 87, 57, 93}
ex2 = {-64, -54, -83, 14, 45, -16, -44, 87, -40, -36}

res1 = main(ex1)
res2 = main(ex2)
print(res1, res2)
