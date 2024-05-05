def true_false(tablet):
    for row in tablet:
        if row[0].startswith('да'):
            row[2] = 'true'
        else:
            row[2] = 'false'
        row[0] = row[0].split('#', 1)[1]
        row[0] = row[0].replace(',', '')
        row[1], row[2] = row[2], row[1]
        row[0] = row[0][:-2]
        row[2] = row[2].replace('-', '.')
        row[3] = row[3].split('@', 1)[1]
    return tablet


def sort_table(tablet):
    return sorted(tablet, key=lambda x: x[0])


def main(tablet1):
    tablet = [row[:] for row in tablet1]
    tablet = true_false(tablet)
    sorted_tablet = sort_table(tablet)
    return sorted_tablet


table1 = [
    ['нет#Софудин, А.Р.', '10-02-01', None, 'sofudin78@gmail.com'],
    ['да#Сумский, В.Ф.', '03-06-00', None, 'sumskij84@gmail.com'],
    ['нет#Рененов, М.О.', '11-01-99', None, 'renenov70@yandex.ru'],
    ['нет#Весян, К.Н.', '18-08-99', None, 'vesan30@mail.ru'],
]

table2 = [
    ['нет#Мешян, И.Ш.', '15-07-04', None, 'mesan32@gmail.com'],
    ['да#Табак, Д.Б.', '12-04-02', None, 'tabak2@yandex.ru'],
    ['нет#Лафеков, С.Ш.', '05-05-03', None, 'lafekov38@yandex.ru'],
]

table3 = (['да#Гутугман, Н.К.', '22-01-99', None, 'gutugman4@yandex.ru'],
          ['нет#Савли, А.К.', '22-04-03', None, 'savli43@mail.ru'],
          ['да#Тумий, Г.Н.', '21-03-01', None, 'tumij96@yandex.ru'],
          ['нет#Гарман, Н.В.', '01-07-04', None, 'garman77@mail.ru'])

tablet = main(table1)

# Определяем максимальную длину каждого столбца
max_lengths = [max(len(str(row[i])) for row in tablet) for i in range(len(tablet[0]))]

# Выводим таблицу
for row in tablet:
    for i in range(len(row)):
        print(str(row[i]).ljust(max_lengths[i] + 2), end="")
    print()

print()
tablet2 = main(table2)

# Определяем максимальную длину каждого столбца
max_lengths = [max(len(str(row[i])) for row in tablet2) for i in range(len(tablet2[0]))]

# Выводим таблицу
for row in tablet2:
    for i in range(len(row)):
        print(str(row[i]).ljust(max_lengths[i] + 2), end="")
    print()

print()
tablet3 = main(table3)

# Определяем максимальную длину каждого столбца
max_lengths = [max(len(str(row[i])) for row in tablet3) for i in range(len(tablet3[0]))]

# Выводим таблицу
for row in tablet3:
    for i in range(len(row)):
        print(str(row[i]).ljust(max_lengths[i] + 2), end="")
    print()
