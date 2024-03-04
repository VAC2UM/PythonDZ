# Второе по популярности решение
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

# print(main(['FLUX', 1976, 'VALA', 'TEA', 'CSS']))
# print(main(['FLUX', 1976, 'OOC', 'VHDL', 'P4']))
# print(main(['DART', 1976, 'OOC', 'HLSL', 'CSS']))
# print(main(['FLUX', 1976, 'ELM', 'VHDL', 'CSS']))
# print(main(['DART', 1988, 'OOC', 'VHDL', 'CSS']))