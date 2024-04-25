import math


def main(z, x, y):
    path1 = (math.sin(55 * x - 87 * z ** 3)) ** 3
    path2 = 83 * (math.sqrt(z - y ** 2)) ** 6
    path3up = (73 + x + 74 * z ** 2) ** 4 - (1 + 42 * y ** 3) ** 7
    path3down = 83 * (x ** 2 / 13 + y ** 3 + 64 * z)
    return path1 + path2 + (path3up / path3down)


print(main(0.24, 0.51, -0.01))
