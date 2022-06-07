import requests
import xml.etree.ElementTree as ET


list_a = ["python"]  # aranacak kelimeyi giriniz
list_b = [" ", "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l",
          "m", "n", "o" "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "x", "q", "w"]  # Harf veya Kelime Ekleyebilirsiniz
list_c = [f"{i} {j}" for i in list_a for j in list_b]

for x in list_c:
    apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=tr&q=" + \
        x  # Google Suggest API
    r = requests.get(apiurl)
    tree = ET.fromstring(r.text)

    for child in tree.iter('suggestion'):
        data = child.attrib['data'], "\n"
        dosya = open("keywords_data.xls", "a+")
        dosya.writelines(data)
