# Первое по полуярности
# from math import floor, tan


# def main(z):
#     if z < -30:
#         z = pow((36 * pow(z, 2) - z - (pow(z, 3) / 89)), 6)
#     elif z >= -30 and z < 22:
#         z = pow(floor(z), 5)
#     elif z >= 22 and z < 64:    
#         z1 = (15 * pow((z - (18 * pow(z, 3)) - (74 * pow(z, 2))), 4))
#         z2 = 1 + pow(((z/33) + 55), 2)
#         z = z1 + z2
#     elif z >= 64 and z < 125:
#         z = 32 * tan(z) - 1
#     elif z >= 125:
#         z = pow(z, 3) + 0.02
#     return z

# print(main(40))

# Второе по полуярности (не сработало)
# from math import floor, tan

# def a(z):
#     return (pow((36 * pow(z, 2) - z - (pow(z, 3) / 89)), 6))
# def b(z)->float:
#     return (pow(floor(z), 5))
# def c(z)->float:
#     return (15 * pow((z - (18 * pow(z, 3)) - (74 * pow(z, 2))), 4)) + 1 + pow(((z/33) + 55), 2)
# def d(z)->float:
#     return (32 * tan(z) - 1)
# def e(z)->float:
#     return (pow(z, 3) + 0.02)
# def main(z):
#     if z < -30:
#         return a(z)
#     elif z >= -30 and z < 22:
#         return b(z)
#     elif z >= 22 and z < 64:    
#         return c(z)
#     elif z >= 64 and z < 125:
#         return d(z)
#     elif z >= 125:
#         return e(z)

# print(main(40))

# Второе по полуярности (не работает)
from math import floor, tan

def prac1(z):
    if z >= 22 and z < 64:    
        z1 = (15 * pow((z - (18 * pow(z, 3)) - (74 * pow(z, 2))), 4))
        z2 = 1 + pow(((z/33) + 55), 2)
        return z1 + z2
    elif z >= 64 and z < 125:
        return 32 * tan(z) - 1
    elif z >= 125:
        return pow(z, 3) + 0.02
    
def main(z):
    return (
        pow((36 * pow(z, 2) - z - (pow(z, 3) / 89)), 6)
        if z < -30
        else prac1(z)
    )

print(main(-25))

# Третье по поулярности
# from math import floor, tan


# def main(z):
#     conditions = {
#         z < -30: lambda: pow((36 * pow(z, 2) - z - (pow(z, 3) / 89)), 6),
#         -30 <= z < 22: lambda: pow(floor(z), 5),
#         22 <= z < 64:
#         lambda:
#         (15 * (z - (18 * z**3) - (74 * z**2))**4) + 1 + ((z/33) + 55)**2,
#         64 <= z < 125: lambda: 32 * tan(z) - 1,
#         z >= 125: lambda: pow(z, 3) + 0.02
#     }
#     for condition, expression in conditions.items():
#         if condition:
#             return expression()

# result = main(40)
# print(result)