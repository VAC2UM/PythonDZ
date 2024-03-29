def main(x):
    x = int(x)
    m1 = x & 0b11
    m3 = (x >> 8) & 0b111_111_111
    m4 = (x >> 17) & 0b111_11
    result = (m1, m3, m4)
    return result

print(main('3691684'))
print(main('1287796'))