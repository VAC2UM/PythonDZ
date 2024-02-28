# Самое популярное решение
# import math


# def main(x, y):
#     n = len(x)
#     y.insert(0, 0)
#     x.insert(0, 0)
#     summa = 0
#     for i in range(1, n + 1):
#         left = 71 * pow(y[n + 1 - math.ceil(i / 4)], 2)
#         right = 50 * pow(x[math.ceil(i / 3)], 3)
#         summa += (left - right) ** 7
#     return 35 * summa

# print(main([0.7, -0.25, -0.01], [-0.7, -0.81, -0.63]))
# ответ 2085404586.062392



# Третье по популярнотси
# import math

# def main(x, y):
#     n = len(x)
#     y.insert(0, 0)
#     x.insert(0, 0)
#     summa = 0
#     i = 1
#     while i <= n:
#         left = 71 * pow(y[n + 1 - math.ceil(i / 4)], 2)
#         right = 50 * pow(x[math.ceil(i / 3)], 3)
#         summa += (left - right) ** 7
#         i += 1
#     return 35 * summa

# Четвертое по популярности решение
# import math

# def calculate_sum_recursive(x, y, i, n, acc):
#     if i > n:
#         return acc
#     left = 71 * pow(y[n + 1 - math.ceil(i / 4)], 2)
#     right = 50 * pow(x[math.ceil(i / 3)], 3)
#     acc += (left - right) ** 7
#     return calculate_sum_recursive(x, y, i + 1, n, acc)

# def main(x, y):
#     n = len(x)
#     y.insert(0, 0)
#     x.insert(0, 0)
#     return 35 * calculate_sum_recursive(x, y, 1, n, 0)