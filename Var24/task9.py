def main(text):
    begin_index = text.find('begin') + len('begin')
    end_index = text.find('end')
    data_section = text[begin_index:end_index]
    pairs = [pair.strip().split('@')
             for pair in data_section.split('set') if pair.strip()]
    result = [(name.strip(), value.strip()) for name, value in pairs]
    cleaned_data = [(name, value.strip(".'")) for name, value in result]
    return cleaned_data


input_string = "begin set getiri @'soed_92'. set arla_890 @'quxe'. set erle_404 @'are'. end"
print(main(input_string))

input_string = "begin set geer_603 @'dite'. set ceon_170 @'orve'. end"
print(main(input_string))
