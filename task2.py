import xml.etree.ElementTree as ET

DATA = "currency.xml"

def scraping(Data):
  tree = ET.parse(Data)
  root = tree.getroot()
  _list_ = []
  valutes = root.findall('Valute')

  for val in valutes:
      code = val.find('CharCode').text
      nominal = val.find('Nominal').text
      if int(nominal) == 10 or int(nominal) == 100:
         _list_.append(code)
  return _list_


if __name__ == '__main__':
  result = scraping(DATA)
  print(result)