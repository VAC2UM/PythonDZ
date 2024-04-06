# Самое популярное  решение
# -------------------------------------------------------------------
# import re
#
#
# def main(data):
#     # Регулярное выражение для извлечения ключей и значений
#     pattern = r'option\s+([\w_]+)\s*:\s*([\w_]+)'
#
#     # Используем findall для поиска всех совпадений
#     matches = re.findall(pattern, data)
#
#     # Создаем словарь из найденных совпадений
#     result = {key: value for key, value in matches}
#
#     return result
# -------------------------------------------------------------------


def main(input_string):
    result = {}
    input_string = input_string.replace('.begin option', ' ')
    input_string = input_string.replace('. option', ',')
    input_string = input_string.replace(':', ':')
    input_string = input_string.replace('. .end', '')

    pairs = input_string.split(',')
    for pair in pairs:
        key, value = pair.split(':')
        result[key.strip()] = value.strip()

    return result


print(main('.begin option abe_117 : ceis. option radior_155 :laenxe_853. option reza_100 :tiat_46. option inzaso_768: sosous_708. .end'))