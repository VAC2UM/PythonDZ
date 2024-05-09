def remove_first_seven(tablet1):
    for row in tablet1:
        row[1] = row[1][7:] if len(row[1]) > 7 else row[1]
        row[1] = row[1].replace('-', '')
    return tablet1


def move_text_after_symbol(tablet1, symbol='|'):
    for row in tablet1:
        if symbol in row[1]:
            index = row[1].index(symbol)
            row.append(row[1][index + 1:])
            row[1] = row[1][:index]
        else:
            row.append('')
    return tablet1


def remove_after_at(tablet1):
    for row in tablet1:
        if len(row) > 2:
            row[2] = row[2].split('@')[0]
    return tablet1


def main(tablet1):
    tablet = [row[:] for row in tablet1]
    remove_first_seven(tablet)
    move_text_after_symbol(tablet)
    tablet = remove_after_at(tablet)
    tablet = [list(row) for row in zip(*tablet)]
    return tablet


table1 = [
    ['нет', '+7(245)114-78-99|tivev92@yandex.ru'],
    ['да', '+7(003)823-94-48|relic73@rambler.ru'],
    ['нет', '+7(384)921-48-37|fizan84@yahoo.com'],
    ['нет', '+7(010)868-27-36|cukuranz23@gmail.com'],
]

print(main(table1))
