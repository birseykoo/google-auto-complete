from sqlite3 import Row
from token import NEWLINE
import requests
import pandas as pd
import string
import xml.etree.ElementTree as ET


list_a = ["aranacak kelime","aranacak kelime"]
list_b = [" ", "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l",
          "m", "n", "o" "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "x", "q", "w"]
list_c = [f"{i} {j}" for i in list_a for j in list_b]

for x in list_c:
    apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=tr&q="+x
    r = requests.get(apiurl)
    tree = ET.fromstring(r.text)
    
    for child in tree.iter('suggestion'):
        data = child.attrib['data'], "\n"
        dosya = open("keywords_data.xls","a+")
        dosya.writelines(data)
        








