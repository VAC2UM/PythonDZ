def main(x):
    n1 = (x >> 0) & 0b1
    n3 = (x >> 4) & 0b111
    n4 = (x >> 7) & 0b1111

    result = int((n1 << 10) | (n3 << 7) | (n4 << 0))
    return result


print(main(1437))
print(main(1534))
print(main(1701))
print(main(1972))