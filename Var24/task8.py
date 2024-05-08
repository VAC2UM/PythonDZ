# def main(arr):
#     l2 = int(arr[1][1]) & 0b11
#     l1 = arr[0][1] & 0b1111
#     res = (l1 << 0) | (l2 << 7)
#     return res
def main(data):
    result = 0
    for field, value in data:
        if field == 'L1':
            result |= value
        elif field == 'L2':
            result |= value << 7
        elif field == 'L4':
            result |= value << 19
        elif field == 'L5':
            result |= value << 20
        elif field == 'L6':
            result |= value << 21
    return str(result)


print(main([('L1', 85), ('L2', 6), ('L4', 0), ('L5', 0), ('L6', 6)]))
print(main([('L1', 84), ('L2', 35), ('L4', 1), ('L5', 0), ('L6', 7)]))
print(main([('L1', 52), ('L2', 49), ('L4', 0), ('L5', 0), ('L6', 7)]))
print(main([('L1', 70), ('L2', 37), ('L4', 1), ('L5', 1), ('L6', 2)]))
