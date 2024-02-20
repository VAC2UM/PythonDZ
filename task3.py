# Первое по популярности
# def main(b, a, p):
#     summa = 0
#     for k in range(1, a+1):
#         for i in range(1, b+1):
#             summa += (15 * pow((p - 18 * pow(p, 3) - 74 * pow(i, 2)), 4)) + 1 + pow((k/33 + 55), 2)
   
#     return summa

# Второе по поулярности
# def main(b, a, p):
#     sum_part = sum(
#         (15 * pow((p - 18 * pow(p, 3) - 74 * pow(i, 2)), 4))
#         + 1 + pow((k/33 + 55), 2)
#         for k in range(1, a + 1)
#         for i in range(1, b + 1))
#     return sum_part


# Пятое по поулярности
# from functools import reduce


# def main(b, a, p):
#     indices = [(k, i) for k in range(1, a + 1) for i in range(1, b + 1)]

#     def compute_value(acc, idx):
#         k, i = idx
#         return acc + ((15 * pow((p - 18 * pow(p, 3) - 74 * pow(i, 2)), 4)) + 1 + pow((k/33 + 55), 2))

#     result = reduce(compute_value, indices, 0)
#     return result

# Четвертое по поулярности
# def main(b, a, p):
#     result = 0
#     k, i = 1, 1

#     while k <= a:
#         while i <= b:
#             result += (15 * pow((p - 18 * pow(p, 3) - 74 * pow(i, 2)), 4)) + 1 + pow((k/33 + 55), 2)
#             i += 1
#         k += 1
#         i = 1

#     return result

# Пятое по популярности
# def main(b, a, p, k = 1, i = 1):
#     if k > a:
#         return 0
#     if i > b:
#         return main(b, a, p, k + 1, 1)
#     return ((15 * pow((p - 18 * pow(p, 3) - 74 * pow(i, 2)), 4)) + 1 + pow((k/33 + 55), 2) + main(b, a, p, k, i + 1))