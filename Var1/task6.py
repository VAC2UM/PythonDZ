import math

def main(P):
    A = {p % 3 - 4 * p for p in P if not (-1e9 < p < -25)}

    I = {p ** 3 for p in P if p >= 31 and p <= 60}

    M = I.union(A)

    X = {abs(a) + y for a in A for y in M if (a < y)}

    answ = len(M) - sum(y - 3 * x for y in M for x in X)

    return answ

res1 = main({70, 42, 45, -13, 52, 85, -41, -39, 90, -68})
res2 = main({-61, 70, -20, 92, -48, -49, 86, -40, 60, -97})
print(res1, res2)