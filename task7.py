# Самое популярное решение
# -------------------------------------------------------------------
# def zero(items, left, right):
#     if items[0] == "DART":
#         return right
#     if items[0] == "FLUX":
#         return left


# def one(items, left, right):
#     if items[1] == 1988:
#         return left
#     if items[1] == 1976:
#         return right


# def two(items, left, midd, right):
#     if items[2] == "ELM":
#         return right
#     if items[2] == "VALA":
#         return midd
#     if items[2] == "OOC":
#         return left


# def three(items, left, midd, right):
#     if items[3] == "HLSL":
#         return right
#     if items[3] == "TEA":
#         return midd
#     if items[3] == "VHDL":
#         return left


# def four(items, left, midd, right):
#     if items[4] == "P4":
#         return right
#     if items[4] == "CSS":
#         return midd
#     if items[4] == "TERRA":
#         return left


# def main(items):
#     result = one(
#         items,
#         10,
#         four(
#             items,
#             9,
#             two(items, 8, 7, 6),
#             three(items, zero(items, 5, 4), zero(items, 3, 2),
#                   zero(items, 1, 0)),
#         ),
#     )
#     return result
# -------------------------------------------------------------------

# Второе по популярности решение
# -------------------------------------------------------------------
# s = (
#     {1976, "P4", "HLSL", "DART"},
#     {1976, "P4", "HLSL", "FLUX"},
#     {1976, "P4", "TEA", "DART"},
#     {1976, "P4", "TEA", "FLUX"},
#     {1976, "P4", "VHDL", "DART"},
#     {1976, "P4", "VHDL", "FLUX"},
#     {1976, "CSS", "ELM"},
#     {1976, "CSS", "VALA"},
#     {1976, "CSS", "OOC"},
#     {1976, "TERRA"},
#     {1988}
# )

# def main(r):
#     s1 = set(r)
#     return [i for i in range(len(s)) if not (len(s[i] - s1))][0]
# -------------------------------------------------------------------

# Третье по популярности
# -------------------------------------------------------------------
# def zero(x, left, right):
#     match x[0]:
#         case "DART":
#             return right
#         case "FLUX":
#             return left
#
#
# def one(x, left, right):
#     match x[1]:
#         case 1976:
#             return right
#         case 1988:
#             return left
#
#
# def two(x, left, mid, right):
#     match x[2]:
#         case "ELM":
#             return right
#         case "VALA":
#             return mid
#         case "OOC":
#             return left
#
#
# def three(x, left, mid, right):
#     match x[3]:
#         case "HLSL":
#             return right
#         case "TEA":
#             return mid
#         case "VHDL":
#             return left
#
#
# def four(x, left, mid, right):
#     match x[4]:
#         case "P4":
#             return right
#         case "CSS":
#             return mid
#         case "TERRA":
#             return left
#
#
# def main(x):
#     result = one(
#         x, 10, four(
#             x, 9, two(
#                 x, 8, 7, 6),
#             three(
#                 x, zero(
#                     x, 5, 4
#
#                 ), zero(
#                     x, 3, 2
#                 ), zero(
#                     x, 1, 0
#                 )
#             )
#
#         )
#     )
#     return result
# -------------------------------------------------------------------

# Четвертое по популярности
# -------------------------------------------------------------------
# s = [
#     {1976, "P4", "HLSL", "DART"},
#     {1976, "P4", "HLSL", "FLUX"},
#     {1976, "P4", "TEA", "DART"},
#     {1976, "P4", "TEA", "FLUX"},
#     {1976, "P4", "VHDL", "DART"},
#     {1976, "P4", "VHDL", "FLUX"},
#     {1976, "CSS", "ELM"},
#     {1976, "CSS", "VALA"},
#     {1976, "CSS", "OOC"},
#     {1976, "TERRA"},
#     {1988}
# ]

# def main(r):
#     s1 = set(r)
#     for i, v in enumerate(s):
#         if not(len(v - s1)):
#             return i
# -------------------------------------------------------------------


# Пятое по популярности
# -------------------------------------------------------------------
# class tree():
#     def __init__(self, number, top, topcon, mid, midcon, down, downcon):
#         self.number = number
#         self.top = top
#         self.mid = mid
#         self.down = down
#         self.topCon = topcon
#         self.midCon = midcon
#         self.downCon = downcon
#
#     def find(self, mas: list, ):
#         if self.top == mas[self.number]:
#             if (type(self.topCon) == int):
#                 return self.topCon
#             return self.topCon.find(mas)
#         if self.mid == mas[self.number]:
#             if (type(self.midCon) == int):
#                 return self.midCon
#             return self.midCon.find(mas)
#         if self.down == mas[self.number]:
#             if (type(self.downCon) == int):
#                 return self.downCon
#             return self.downCon.find(mas)
#
#
# def main(mas):
#     x01 = tree(0,
#                "DART", 0, None, None, "FLUX", 1)
#     x02 = tree(0,
#                "DART", 2, None, None, "FLUX", 3)
#     x03 = tree(0,
#                "DART", 4, None, None, "FLUX", 5)
#     x2 = tree(2,
#               "ELM", 6, "VALA", 7, "OOC", 8)
#     x3 = tree(3,
#               "HLSL", x01, "TEA", x02, "VHDL", x03)
#     x4 = tree(4,
#               "P4", x3, "CSS", x2, "TERRA", 9)
#     x1 = tree(1,
#               1976, x4, None, None, 1988, 10)
#     return x1.find(mas)
# -------------------------------------------------------------------

# print(main(['FLUX', 1976, 'VALA', 'TEA', 'CSS']))
# print(main(['FLUX', 1976, 'OOC', 'VHDL', 'P4']))
# print(main(['DART', 1976, 'OOC', 'HLSL', 'CSS']))
# print(main(['FLUX', 1976, 'ELM', 'VHDL', 'CSS']))
# print(main(['DART', 1988, 'OOC', 'VHDL', 'CSS']))