import struct


def read_int8(data, offset):
    return struct.unpack_from('>b', data, offset)[0], offset + 1


def read_int16(data, offset):
    return struct.unpack_from('>h', data, offset)[0], offset + 2


def read_int32(data, offset):
    return struct.unpack_from('>i', data, offset)[0], offset + 4


def read_uint8(data, offset):
    return struct.unpack_from('>B', data, offset)[0], offset + 1


def read_uint16(data, offset):
    return struct.unpack_from('>H', data, offset)[0], offset + 2


def read_uint32(data, offset):
    return struct.unpack_from('>I', data, offset)[0], offset + 4


def read_uint64(data, offset):
    return struct.unpack_from('>Q', data, offset)[0], offset + 8


def read_double(data, offset):
    return struct.unpack_from('>d', data, offset)[0], offset + 8


def read_float(data, offset):
    return struct.unpack_from('>f', data, offset)[0], offset + 4


def read_structure_B(data, offset):
    b1, offset = read_int32(data, offset)
    b2, offset = read_double(data, offset)
    b3, offset = read_int16(data, offset)
    b4, offset = read_int16(data, offset)
    b5, offset = read_float(data, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}, offset


def read_structure_C(data, offset):
    c1_size, offset = read_uint16(data, offset)
    c1_address, offset = read_uint32(data, offset)
    # Проверим, что считанные адрес и размер находятся в пределах данных
    if c1_address + c1_size > len(data):
        raise ValueError("Array size or address is out of the data bounds")
    c1 = list(struct.unpack_from(f'>{c1_size}f', data, c1_address))

    c2, offset = read_float(data, offset)
    return {'C1': c1, 'C2': c2}, offset


def main(data):
    if data[:3] != b'LJF':
        raise ValueError("Invalid data signature")
    offset = 4
    a1, offset = read_uint64(data, offset)
    a2_size, offset = read_uint32(data, offset)
    a2_address, offset = read_uint32(data, offset)
    # Проверим, что считанные адрес и размер находятся в пределах данных
    if a2_address + a2_size > len(data):
        raise ValueError("Array size or address is out of the data bounds")
    a2 = list(struct.unpack_from(f'>{a2_size}c', data, a2_address))
    a2 = b''.join(a2).decode('utf-8')

    a3, offset = read_structure_B(data, offset)
    a4, offset = read_int8(data, offset)
    a5, offset = read_double(data, offset)

    # Чтение размера и адреса массива структур C
    a6_size, offset = read_uint16(data, offset)
    a6_address, offset = read_uint32(data, offset)
    if a6_address + a6_size > len(data):
        raise ValueError("Array size or address is out of the data bounds")

    a6 = []
    for i in range(a6_size):
        c_struct, offset = read_structure_C(data,
                                            a6_address + i * 10)
        a6.append(c_struct)

    a7_offset = struct.unpack('>h', data[offset:offset + 2])[0]
    offset += 2
    d1_size, offset = read_uint32(data, offset)
    d1_address, offset = read_uint16(data, offset)
    if d1_address + d1_size > len(data):
        raise ValueError("Array size or address is out of the data bounds")
    d1 = list(struct.unpack_from(f'>{d1_size}B', data, d1_address))
    d2, offset = read_int8(data, offset)
    d3, offset = read_int8(data, offset)
    d4, offset = read_uint8(data, offset)

    a7 = {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}

    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}


print(main(b'LJFm\x11ycb\x00\x82%~\x00\x00\x00\x02\x00\x00\x0092\xfc\x0f\xf0\xbf\xeeX_'
           b'\xc7\xbd-\xb6\xb5\x15F\x1d?&\x9e?\xeb?\xe1\xfcpfg\x00r\x00\x05\x00'
           b'\x00\x00c\x00\x97kg\xbfc!\xbf>\xee\x16!?CY\xda\xbd\xe2S)?P\x10!\xbe'
           b' \xca\x80\xbd\xe9\xea\xbe\xbe\xc3\xdf\x04?q\xf9\x94\xbf!\xdb"\x00'
           b'\x02\x00\x00\x00;>\x95\xa5\xa2\x00\x02\x00\x00\x00C?U\xf4K\x00'
           b'\x02\x00\x00\x00K?|a\x10\x00\x02\x00\x00\x00S?\x11Pm\x00\x02\x00\x00\x00'
           b'[?p\xdb\xaa\xd7c\x00\x00\x00\x02\x00\x95\x9d\x92\xee'))
