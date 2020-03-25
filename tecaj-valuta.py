import xml.etree.ElementTree as ET
import requests
import re

datum_tecaja = input('Vnesi datum tečajnice (LLLL-MM-DD): ')
valuta = input('Vnesi oznako valute (npr. USD): ').upper()

r = requests.get('https://www.bsi.si/_data/tecajnice/dtecbs-l.xml')
if r.status_code == 200:
    # remove namespace
    xmlstring = re.sub(' xmlns="[^"]+"', '', r.content.decode('utf-8'), count=1)
    root = ET.fromstring(xmlstring)
        
    for dat_tecaj in root.iter('tecajnica'):
        if dat_tecaj.attrib['datum'] == datum_tecaja:
            for tecaj_valuta in dat_tecaj.iter('tecaj'):
                if tecaj_valuta.attrib['oznaka'] == valuta:
                    print('Tečaj za valuto ' + valuta + ' na dan: ' + datum_tecaja + ' je: ' + tecaj_valuta.text)
                