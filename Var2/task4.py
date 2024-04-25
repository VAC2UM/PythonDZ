import math


def main(n):
    if n == 0:
        return 1.00
    elif n == 1:
        return 0.33
    elif n >= 2:
        return ((math.ceil(float(main(n - 2)))) ** 2 +
                0.01 + 2 * float(main(n - 1)))


print(main(3))
print(main(9))
print(main(7))
print(main(5))
print(main(8))
