# Самое популярное решение
# -------------------------------------------------------------------
def zero(items, left, right):
    if items[0] == "DART":
        return right
    if items[0] == "FLUX":
        return left


def one(items, left, right):
    if items[1] == 1988:
        return left
    if items[1] == 1976:
        return right


def two(items, left, midd, right):
    if items[2] == "ELM":
        return right
    if items[2] == "VALA":
        return midd
    if items[2] == "OOC":
        return left


def three(items, left, midd, right):
    if items[3] == "HLSL":
        return right
    if items[3] == "TEA":
        return midd
    if items[3] == "VHDL":
        return left


def four(items, left, midd, right):
    if items[4] == "P4":
        return right
    if items[4] == "CSS":
        return midd
    if items[4] == "TERRA":
        return left


def main(items):
    result = one(
        items,
        10,
        four(
            items,
            9,
            two(items, 8, 7, 6),
            three(items, zero(items, 5, 4), zero(items, 3, 2),
                  zero(items, 1, 0)),
        ),
    )
    return result
# -------------------------------------------------------------------
