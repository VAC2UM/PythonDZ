# Самое популярное решение
#-------------------------------------------------------------------
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
#-------------------------------------------------------------------

# Второе по популярности решение
#-------------------------------------------------------------------
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
#-------------------------------------------------------------------

# Четвертое по популярности
#-------------------------------------------------------------------
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
#-------------------------------------------------------------------

# print(main(['FLUX', 1976, 'VALA', 'TEA', 'CSS']))
# print(main(['FLUX', 1976, 'OOC', 'VHDL', 'P4']))
# print(main(['DART', 1976, 'OOC', 'HLSL', 'CSS']))
# print(main(['FLUX', 1976, 'ELM', 'VHDL', 'CSS']))
# print(main(['DART', 1988, 'OOC', 'VHDL', 'CSS']))