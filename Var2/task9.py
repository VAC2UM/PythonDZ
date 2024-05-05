import re


def main(data):
    pattern = r'make\s+@"(\w+)"\s*:\s*array\(\s*([^)]+)\s*\)'
    matches = re.findall(pattern, data)
    result = [(key, [item.strip() for item in value.split('.')])
              for key, value in matches]
    return result


input_string = r'\begin <section>make @"orarige_480" :array( enanle . atin . isbe . bitele_859 ).</section>; <section> make @"veveed" : array( erdi . ante_639 . bedi_923 . soso). </section>;\end'
input_string2 = r'\begin <section> make @"ququ_737" : array(xeaxe_346 . isen_364). </section>; <section> make @"bireed_749" : array(rais . onve . arer . geace_238). </section>; <section> make @"orri_317" :array( xeri_456 . zatite_819).</section>;\end'
print(main(input_string))
print(main(input_string2))
