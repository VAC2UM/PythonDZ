import struct


def read_char(data, offset):
    return struct.unpack_from('>c', data, offset)[0], offset + 1


def read_int8(data, offset):
    return struct.unpack_from('>b', data, offset)[0], offset + 1


def read_int16(data, offset):
    return struct.unpack_from('>h', data, offset)[0], offset + 2


def read_int64(data, offset):
    return struct.unpack_from('>q', data, offset)[0], offset + 8


def read_uint8(data, offset):
    return struct.unpack_from('>B', data, offset)[0], offset + 1


def read_uint16(data, offset):
    return struct.unpack_from('>H', data, offset)[0], offset + 2


def read_uint32(data, offset):
    return struct.unpack_from('>I', data, offset)[0], offset + 4


def read_structure_С(data, offset):
    c1, offset = read_int16(data, offset)
    c2 = []
    for _ in range(5):
        element, offset = read_uint16(data, offset)
        c2.append(element)
    c3, offset = read_uint8(data, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def read_structure_D(data, offset):
    d1, offset = read_int8(data, offset)
    d2, offset = read_int64(data, offset)
    d3_size, offset = read_uint32(data, offset)
    d3_address, offset = read_uint16(data, offset)

    # Проверим, что считанные адрес и размер находятся в пределах данных
    if d3_address + d3_size > len(data):
        raise ValueError("Array size or address is out of the data bounds")

    d3 = list(struct.unpack_from(f'>{d3_size}B', data, d3_address))
    d4 = []
    for _ in range(3):
        element, offset = read_int8(data, offset)
        d4.append(element)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def read_structure_E(data, offset):
    e1, offset = read_uint16(data, offset)
    e2, offset = read_uint8(data, offset)
    return {'E1': e1, 'E2': e2}, offset


def read_structure_B(data, offset):
    b1 = []
    for _ in range(6):
        element, offset = read_structure_С(data, offset)
        b1.append(element)
    b2, offset = read_structure_D(data, offset)
    b3, offset = read_structure_E(data, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def main(data):
    if data[:3] != b'BED':
        raise ValueError("Invalid data signature")
    offset = 3
    a1 = []
    for _ in range(5):
        element, offset = read_char(data, offset)
        a1.append(element)

    a1 = b''.join(a1).decode('utf-8')
    a2, offset = read_structure_B(data, offset)
    return {'A1': a1, 'A2': a2}


print(main(b'BEDsxacl\xa3T\x0e\xcdh\x8d\xe2QN4\x1c+3a+\x0b\xcf25v\xa34\xf3\x03'
           b'\x8d\xd1:\x9c\xf4\xe6\x90\xb0X\xb9\xadd=B\t\xc6\xf7\xa3\xdaV`\xbc\xd4\x06'
           b'>\xc2\xe2\xef\xcaK\x9c<|\x91n\xe3\x8d079 \xc6\xa6\xa8\x92;\xaa\x84q\x89a&'
           b'7\xfc?h\x8d\xc0\x1e\x0b\xe0_\xe1\x00\x00\x00\x03\x00k\x8a\xf9\x81z\xd2\x8dA'
           b'\xe7;'))
