# Самое популярное решение
# def main(z, x):
#     n = len(z)
#     z.insert(0, 0)
#     x.insert(0, 0)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += (51 * (z[i] + z[i] ** 3
#         + 24 * x[i] ** 2) ** 6)
#     return 88 * summa

# Второе по поулярности
# def main(z, x):
#     n = len(z)
#     z.insert(0, 0)
#     x.insert(0, 0)
#     return 88 * sum((51 * (z[i] + z[i] ** 3 + 24 * x[i] ** 2) ** 6) for i in range(1, n + 1))

# Третье по популярности
# def main(z, x):
#     n = len(z)
#     z.insert(0, 0)
#     x.insert(0, 0)
#     summa = 0
#     i = 1
#     while i <= n:
#         summa += (51 * (z[i] + z[i] ** 3 + 24 * x[i] ** 2) ** 6)
#         i += 1
#     return 88 * summa

# Четвертое по популярности
# def calculate_sum_recursive(z, x, i, n, acc):
#     if i > n:
#         return acc
#     else:
#         return calculate_sum_recursive(z, x, i + 1, n, acc + (51 * (z[i] + z[i] ** 3 + 24 * x[i] ** 2) ** 6))

# def main(z, x):
#     n = len(z)
#     z.insert(0, 0)
#     x.insert(0, 0)
#     summa = calculate_sum_recursive(z, x, 1, n, 0)
#     return 88 * summa

# print(main([0.78, -0.14, -0.95, -0.69, -0.53, -0.63, 0.09, 0.82], [-0.31, 0.29, -0.98, 0.35, -1.0, -0.45, 0.8, -0.05]))