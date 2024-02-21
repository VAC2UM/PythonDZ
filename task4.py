# Самое популярное решение
# def main(n):
#     if n == 0:
#         return 0.74
#     elif n == 1:
#         return -0.92
#     elif n >= 2:
#         return 1 + main(n - 2) ** 4 + main(n - 1)

# Второе по популярности
# def main(n):
#     a, b = 0.74, -0.92
#     for _ in range(n):
#         a, b = b, 1 + (a ** 4) + b
#     return a

# Третье по популярности
# def main(n):
#     values = [0.74, -0.92]

#     for i in range(2, n + 1):
#         values.append(1 + values[i - 2] ** 4 + values[i - 1])

#     return values[n]

# Четвертое по поулярности
def main(n):
    return (
        0.74 if n == 0 else
        -0.92 if n == 1 else
        1 + main(n - 2) ** 4 + main(n - 1)
    )
print(main(2))  # Выведет значение для n = 10

# Пятое по популярности
# def main(n):
#     return (
#         0.74 if n == 0 else
#         -0.92 if n == 1 else
#         (lambda x: 1 + x[0]**4 + x[1])([main(n - 2), main(n - 1)])
#     )