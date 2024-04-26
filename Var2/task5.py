def main(x, y, z):
    n = len(x)
    x.insert(0, 0)
    y.insert(0, 0)
    z.insert(0, 0)
    summa = 0
    for i in range(1, n + 1):
        left = y[n + 1 - i] ** 3
        mid = x[n + 1 - i] ** 2
        right = z[n + 1 - i]
        summa += 51 * (left + mid + right) ** 6
    return summa


print(main([-0.47, -0.06, 0.98],
           [0.95, 0.76, -0.99],
           [-0.89, -0.36, -0.01]))
print(main([-0.87, -0.25, -0.47],
           [0.55, -0.52, -0.16],
           [0.8, -0.29, 0.08]))
print(main([-0.61, -0.9, -0.16],
           [0.83, 0.62, -0.69],
           [-0.41, 0.85, 0.65]))
print(main([0.34, -0.84, -0.56],
           [-0.55, 0.26, -0.4],
           [-0.57, 0.87, -0.17]))
