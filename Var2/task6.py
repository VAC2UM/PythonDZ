import math


def main(input_set):
    K = {e ** 2 + 4 * e for e in input_set if (29 > e > -26)}

    A = {e % 2 + abs(e) for e in input_set if (e < 45 or e >= -16)}

    X = {abs(a) for a in A if not (-1e9 < a < 72)}

    T = {math.ceil(x / 7) + x % 3 for x in X if (x >= -86 or x < 27)}

    Ix = {b - math.ceil(x / 6) for b in K for x in X if b > x}

    answ = len({(a, b) for a in Ix for b in T}) - sum(abs(t) for t in T)

    return answ


res1 = main({98, 6, -5, -84, -20, 17, 18, 51, -73, 27})
res2 = main({-61, 71, 8, 11, -84, -80, 81, 51, 56, 58})
print(res1, res2)
