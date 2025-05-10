import requests
from bs4 import BeautifulSoup
import json

print('Web scraping')
print("Exercises")
print("1-")


url1 = "http://www.bu.edu/president/boston-university-facts-stats/"
respuesta1 = requests.get(url1, timeout=8)
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

