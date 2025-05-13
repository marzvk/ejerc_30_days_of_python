import json
import requests
from bs4 import BeautifulSoup
import re

print('Web scraping')
print("Exercises")
print("1-")

URL1 = "http://www.bu.edu/president/boston-university-facts-stats/"
respuesta1 = requests.get(URL1, timeout=8)
# traemos el contenido de la pagina con get
content = respuesta1.content
datos = BeautifulSoup(content, 'html.parser')
resultados1 = datos.find('div', class_="facts-stats-content")
# print(resultados1.prettify())

elementos1 = resultados1.find_all("section", class_="stat-section")

# for elemento in elementos1:
#     titulo = elemento.find("h4", class_="stat-group-title")
#     print(titulo.text)

# solo dos titulos falta campus pero esta nombrado con otra class,
# y no esta dentro de un section como estos

# ESA DIRECCION NO ES LA Q TIENE LA TABLA,  la siguiente si

URL11 = "https://www.bu.edu/about/dna/"
response1 = requests.get(URL11, timeout=8)
content1 = response1.content
datos1 = BeautifulSoup(content1, 'html.parser')
# print(datos1.prettify())
tables = datos1.find_all('figure', class_="wp-block-table")
# print(table.prettify())
# print(len(tables)) #9

listajs = []
for table in tables:
    dic = {}
    for tr in table.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        if th and td:  # Si existen
            th = th.get_text(strip=True)  # muestra solo el texto
            td = td.get_text(strip=True)
            dic[th] = td
    listajs.append(dic)
JSON_DATA = json.dumps(listajs, indent=4)  # transformado a json

print(JSON_DATA)

#########################################################################
print()
print('2-')
print()
URL2 = 'https://archive.ics.uci.edu/dataset/109/wine'
response2 = requests.get(URL2, timeout=8)
content2 = response2.content
datos2 = BeautifulSoup(content2, 'html.parser')
tables2 = datos2.find('table', class_='table my-4 w-full')
# print(tables2.prettify())

# Obtener los títulos con list compreshion.
# para cada th in tables2.findall hacer texto
titulos = [th.get_text(strip=True) for th in tables2.find_all('th')]

# Obtener las filas
filas = []
for tr in tables2.find_all('tr'):
    celdas = [td.get_text(strip=True) for td in tr.find_all('td')]
    if celdas:  # ignora filas vacías
        filas.append(celdas)

# Armar la lista de diccionarios
lista_de_diccionarios = [
    dict(zip(titulos, fila)) for fila in filas if len(fila) == len(titulos)
]

# Mostrar como JSON
print(json.dumps(lista_de_diccionarios, indent=4))

#########################################################################
print()
print('3-')
print()
URL3 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response3 = requests.get(URL3, timeout=8)
content3 = response3.content

datos3 = BeautifulSoup(content3, 'html.parser')
tables3 = datos3.find('table', class_='wikitable')

# print(tables3.prettify())
titulos3 = [th.get_text(strip=True) for th in tables3.find('tr')]


def limpiar_lista(elem):
    elemento = re.sub(r'[\u2010-\u2014\u2013]', '-', elem)
    elemento = re.sub(r'\u00a0', '-', elemento)
    elemento = re.sub(r'\[.*?\]', '', elemento).strip()
    return elemento


titulos3 = [limpiar_lista(e) for e in titulos3 if limpiar_lista(e)]
# print(titulos)
# titulos = [re.sub(r'\[.*?\]', '', item) for item in titulos]
# titulos = [ elem.strip() for elem in titulos if elem.strip()]

filas2 = []
for tr in tables3.find_all('tr'):
    celdas = [td.get_text(strip=True) for td in tr.find_all('td')]
    if celdas:
        filas2.append(celdas)
td3 = []
for sub_list in filas2:
    td3.append([limpiar_lista(e) for e in sub_list if limpiar_lista(e)])

print(json.dumps(titulos3, indent=4))
# dic_list = [dict(zip(titulos3,fila)) for fila in td3 if len(fila) == len(titulos3) ]
print(json.dumps(td3, indent=4))
