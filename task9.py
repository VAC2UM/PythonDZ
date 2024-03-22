def main(x):
    x = x.replace('(', '').replace(')', '').replace('var', '').replace('\n', '').replace(' ', '').replace('|', '').replace('.option', '').replace('.begin', '').replace('.end', '')
    x_parts = x.split(':')
    x_parts = [i for i in x_parts if i]  # удаляем пустые строки из списка
    x_parts1 = []
    for i in x_parts:
        if ':' in i:
            x_parts1.append(i.split(':'))
        else:
            print(f"Ошибка: в строке '{i}' отсутствует двоеточие")
    result = {}
    for i in x_parts1:
        result[i[0]] = i[1]
    return result

print(main(".begin option abe_117 : ceis. option radior_155 :laenxe_853. option reza_100 :tiat_46. option inzaso_768: sosous_708. .end"))
