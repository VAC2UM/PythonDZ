import math


def main(a, n, y, m, b):
    summa = 0
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        for c in range(1, a + 1):
            sum1 += (31 * i ** 7 - 59 * math.exp(63 * y
                                                 + 28 + c ** 2) ** 3)
    for k in range(1, b + 1):
        for i in range(1, m + 1):
            sum2 += (math.tan(i) ** 4 - 1 - 87 *
                     (k - 36 * k ** 2 - i ** 3) ** 5)

    summa = sum1 + sum2
    return "{:.3}".format(summa)


print(main(4, 6, 0.73, 2, 7))
print(main(7, 5, 0.88, 5, 7))
print(main(8, 3, -0.84, 4, 3))
print(main(3, 2, -0.95, 3, 4))
print(main(4, 2, -0.48, 2, 5))
