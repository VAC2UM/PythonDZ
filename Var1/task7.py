# Самое популярное решение
# -------------------------------------------------------------------
# def zero(items, left, right):
#     if items[0] == 2019:
#         return right
#     if items[0] == 1968:
#         return left
#
#
# def one(items, left, right):
#     if items[1] == "HAML":
#         return right
#     if items[1] == "PERL":
#         return left
#
#
# def two(items, left, midd, right):
#     if items[2] == 2019:
#         return right
#     if items[2] == 2004:
#         return midd
#     if items[2] == 2007:
#         return left
#
#
# def three(items, left, midd, right):
#     if items[3] == "LEX":
#         return right
#     if items[3] == "ASN.1":
#         return midd
#     if items[3] == "MTML":
#         return left
#
#
# def main(items):
#     result = zero(
#         items,
#         one(
#             items,
#             three(
#                 items,
#                 9, 8, 7
#             ),
#             two(
#                 items,
#                 6, 5, 4
#             )
#         ),
#         one(
#             items,
#             3,
#             two(
#                 items,
#                 2, 1, 0
#             )
#         )
#     )
#     return result
# -------------------------------------------------------------------


# Второе по популярности решение
# -------------------------------------------------------------------
# Вроде работает
# s = (
#     {2019, "HAML", 2019},
#     {2019, "HAML", 2004},
#     {2019, "HAML", 2007},
#     {2019, "PERL"},
#     {1968, "HAML", 2019},
#     {1968, "HAML", 2004},
#     {1968, "HAML", 2007},
#     {1968, "PERL", "LEX"},
#     {1968, "PERL", "ASN.1"},
#     {1968, "PERL", "MTML"}
# )
#
# def main(r):
#     s1 = set(r)
#     return max([i for i in range(len(s))
#             if not (len(s[i] - s1))])
# -------------------------------------------------------------------


# Третье по популярности
# -------------------------------------------------------------------
# def zero(x, left, right):
#     match x[0]:
#         case 2019:
#             return right
#         case 1968:
#             return left
#
# def one(x, left, right):
#     match x[1]:
#         case "HAML":
#             return right
#         case "PERL":
#             return left
#
# def two(x, left, mid, right):
#     match x[2]:
#         case 2019:
#             return right
#         case 2004:
#             return mid
#         case 2007:
#             return left
#
# def three(x, left, mid, right):
#     match x[3]:
#         case "LEX":
#             return right
#         case "ASN.1":
#             return mid
#         case "MTML":
#             return left
#
# def main(x):
#     result = zero(
#         x, one(
#             x, three(
#                 x, 9, 8, 7
#             ), two(
#                 x, 6, 5, 4
#             )
#         ), one(
#             x, 3, two(
#                 x, 2, 1, 0
#             )
#         )
#     )
#     return result
# -------------------------------------------------------------------


# Четвертое по популярности
# -------------------------------------------------------------------
# Вроде работает
# s = [
#     {2019, "HAML", 2019},
#     {2019, "HAML", 2004},
#     {2019, "HAML", 2007},
#     {2019, "PERL"},
#     {1968, "HAML", 2019},
#     {1968, "HAML", 2004},
#     {1968, "HAML", 2007},
#     {1968, "PERL", "LEX"},
#     {1968, "PERL", "ASN.1"},
#     {1968, "PERL", "MTML"}
# ]
#
# def main(r):
#     s1 = set(r)
#     return max([i for i, v in enumerate(s) if not(len(v - s1))])
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
# def main(mas):
#     x3 = tree(3,
#               "LEX", 7, "ASN.1", 8, "MTML", 9)
#
#     x2_top = tree(2,
#                   2019, 0, 2004, 1, 2007, 2)
#
#     x2_down = tree(2,
#                    2019, 4, 2004, 5, 2007, 6)
#
#     x1_top = tree(1,
#               "HAML", x2_top, None, None, "PERL", 3)
#
#     x1_down = tree(1,
#                    "HAML", x2_down, None, None, "PERL", x3)
#
#     x0 = tree(0,
#               2019, x1_top, None, None, 1968, x1_down
#     )
#
#     return x0.find(mas)
# -------------------------------------------------------------------

print(main([1968, 'PERL', 2004, 'ASN.1']))
print(main([2019, 'PERL', 2007, 'MTML']))
print(main([1968, 'HAML', 2007, 'ASN.1']))
print(main([2019, 'HAML', 2004, 'LEX']))
print(main([1968, 'HAML', 2004, 'ASN.1']))