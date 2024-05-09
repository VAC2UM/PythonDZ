import math


def main(y, x, z):
    n = len(x)
    y.insert(0, 0)
    x.insert(0, 0)
    z.insert(0, 0)
    summa = 0
    for i in range(1, n + 1):
        left = 83 * x[math.ceil(i / 3)] ** 3
        mid = 9 * z[n + 1 - math.ceil(i / 4)]
        right = 38 * y[n + 1 - math.ceil(i / 3)] ** 2

        summa += 2 * math.cos(left - mid - right) ** 7
    return summa


print(main([0.66, 0.75],
           [-0.03, 0.0],
           [0.53, 0.83]))
print(main([-0.02, -0.36],
           [-0.22, 0.41],
           [0.2, 0.52]))
print(main([-0.97, 0.15],
           [0.37, -0.06],
           [-0.79, -0.55]))
print(main([0.86, -0.88],
           [0.05, -0.08],
           [-0.43, 0.75]))
print(main([-0.86, -0.65],
           [0.96, 0.32],
           [0.04, 0.3]))
