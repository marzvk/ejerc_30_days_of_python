import json
import requests
from bs4 import BeautifulSoup

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
