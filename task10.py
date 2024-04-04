# Второе по популярности решение
# -------------------------------------------------------------------
def remove_duplicate_column(tablet):
    for row in tablet:
        if len(row) > 3 and row[2] == row[3]:
            del row[3]


def remove_none_rows(tablet):
    return [row for row in tablet if not all(value is None for value in row)]


def change_phone_number(tablet):
    for row in tablet:
        if row[0] is not None:
            phone_number = row[0]

            phone_number = phone_number.replace("+7 ", "")  # Удаляем "+7 "
            phone_number = "(" + phone_number[:3] + ") " + phone_number[4:]  # Форматируем номер

            row[0] = phone_number


def format_date(date_str):
    parts = date_str.split('/')
    day = parts[2][-2:]
    year = parts[0][-2:]
    return '-'.join([day, parts[1], year])


def split_and_format_date(tablet):
    for row in tablet:
        if row[1] is not None:
            parts = row[1].split('&')
            if len(parts) == 2:
                row[1] = format_date(parts[1])


def extract_name_initials(tablet):
    for row in tablet:
        if row[1] is not None:
            # Получаем фамилию и инициалы из второго столбца
            name_initials = row[1].split('&')[0]

            # Отделяем два последних символа
            name_initials = name_initials[:-2]

            # Записываем их в третий столбец
            row[2] = name_initials


def extract_email(tablet):
    for row in tablet:
        if len(row) > 3 and row[3] is not None:
            # Получаем почту до квадратных скобок
            email = row[3].split('[')[0]

            # Записываем её в четвёртый столбец
            row[3] = email


def main(tablet1):
    tablet = [row[:] for row in tablet1]
    change_phone_number(tablet)
    remove_duplicate_column(tablet)
    extract_name_initials(tablet)
    split_and_format_date(tablet)
    extract_email(tablet)
    tablet = remove_none_rows(tablet)
    return tablet
# -------------------------------------------------------------------


table1 = [
    ['+7 235 048-4098', 'Децулянц Р.Т.&2000/12/28', '+7 235 048-4098', 'dezulanz61[at]mail.ru'],
    ['+7 613 409-1671', 'Чевский В.С.&2000/12/17', '+7 613 409-1671', 'cevskij33[at]yahoo.com'],
    [None, None, None, None],
    ['+7 685 307-8667', 'Роцберг А.О.&2000/05/08', '+7 685 307-8667', 'rozberg84[at]mail.ru'],
]

print(main(table1))
