from math import atan, log


def main(z):
    if z < -6:
        z = 96 * z ** 6
    elif -6 <= z < 18:
        z = (95 * (abs(74 * z ** 2 + 35 * z ** 3 + 30 * z)) ** 5 +
             54 * (log(z, 2)) ** 3 + z ** 7)
    elif z >= 18:
        z = atan(z) ** 4 + 44 * z ** 2
    return z


print(main(90))
