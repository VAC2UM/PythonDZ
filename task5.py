import math


def main(x, y):
    n = len(x)
    y.insert(0, 0)
    x.insert(0, 0)
    summa = 0
    for i in range(1, n + 1):
        left = 71 * pow(y[n + 1 - math.ceil(i / 4)], 2)
        right = 50 * pow(x[math.ceil(i / 3)], 3)
        summa += (left - right) ** 7
    return 35 * summa