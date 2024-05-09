import math


def main(input_set):
    F = {o ** 2 for o in input_set if -1e9 < o < 77}

    On = {f for f in F if f < 64 or f > -56}

    N = input_set.union(F)

    answ1 = sum(math.ceil(v / 5) for v in N)
    answ2 = sum(v * o for v in N for o in On)
    return answ1 + answ2


res1 = main({-95, 44, -50, -48, 81, 19, 20, 24, 26, -68})
res2 = main({69, 38, -25, 9, 41, 28, -46, -45, 60, -67})
print(res1, res2)
