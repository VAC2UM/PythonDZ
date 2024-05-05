def main(data):
    decoded = {}
    decoded['O1'] = str(data & 0b1)

    decoded['O2'] = str((data >> 1) & 0b111_11)

    decoded['O3'] = str((data >> 6) & 0b11_11)

    decoded['O4'] = str((data >> 10) & 0b1)

    decoded['O5'] = str((data >> 11) & 0b111_111_111_1)

    return decoded


print(main(1599933))
print(main(692169))
print(main(1328928))
print(main(1774187))
