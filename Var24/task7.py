s = (
    {"PIKE", 1993, "LASSO"},
    {"PIKE", 1993, "SLIM"},
    {"PIKE", 1993, "SHEN"},
    {"PIKE", 1990, 1968},
    {"PIKE", 1990, 1992},
    {"PIKE", 1990, 1985},
    {"XTEND"},
    {"EQ", 1968, "LASSO"},
    {"EQ", 1968, "SLIM"},
    {"EQ", 1968, "SHEN"},
    {"EQ", 1992},
    {"EQ", 1985}
)


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not (len(s[i] - s1))][0]


print(main([1990, 'SHEN', 'EQ', 1968]))
print(main([1990, 'LASSO', 'PIKE', 1985]))
print(main([1993, 'SLIM', 'PIKE', 1968]))
print(main([1990, 'SHEN', 'PIKE', 1968]))
print(main([1990, 'LASSO', 'PIKE', 1992]))
