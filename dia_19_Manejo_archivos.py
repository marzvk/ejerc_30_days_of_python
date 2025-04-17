import json
import os
import csv
import re

# python dictionary
persona = {"name": "pilar", "pais": "spainn", "addres": ["no se", 'ni idea']}
print(type(persona))
persona_json = json.dumps(persona, indent=4)
print('type de to_json: ', type(persona_json))
print(persona_json)

go_back = json.loads(persona_json)
print(go_back)
print(type(go_back))

with open('./ejemplo.json', "w", encoding='utf-8') as file:
    json.dump(persona, file, ensure_ascii=False, indent=4)
# guardar un dictionaty pasado a json en un archivo con dump()

with open("data_files/my_file.txt", encoding="utf~8") as txt_file:
    contents = txt_file.read()
print('contenido primer linea del txt: ', contents)

txt_file = open("data_files/my_file.txt", "w+")  # r+ leer y ecribir
txt_file.write("moure\napellido\n40\npython\nPYTHON")

# txt_file.close()

for line in txt_file.readlines():
    print(line)

#txt_file.write("\ninformatorio")
#print(txt_file)

with open("data_files/my_file.txt"
          ) as f:  # con with - closes the files by itself
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# os.remove("data_files/my_file.txt")

# # # # #  EJERCICOS LEVEL 1 # # # # # #
print()
print("Exercises Level 1")
print()

# 1 Write a function which count number of lines and number of words in a text


def count_total(filename):
    with open(filename, encoding="utf~8") as f:
        lineas = 0
        palabras = 0
        for line in f.readlines():
            lineas += 1
            coincide = re.sub(r'[$%&#;.?@,!-]', '', line)
            matches = re.split(' ', coincide)
            palabras += len(matches)
            #for palabra in matches:
            #    palabras += 1
        return f'El texto tiene: {lineas} lineas y {palabras} palabras'


print('1- ', count_total(filename="data_files/melina_trump_speech.txt"))

# 2 Read the countries_data.json data file in data directory,
# create a function that finds the ten most spoken languages


def most_spoken_lenguages(filename, number_to_find):
    with open(filename, encoding="utf~8") as f:
        j = f.read()
    diction = json.loads(j)
    language = []
    language_set = set()
    for dic in diction:
        for idiom in dic["languages"]:
            language.append(idiom)
            language_set.add(idiom)
    salida = []
    for idioma in language_set:
        salida.append(((language.count(idioma)), idioma))
    salida.sort(key=lambda a: a[0], reverse=True)
    return salida[0:number_to_find]


print('2- ', most_spoken_lenguages("data_files/countries_data.json", 10))

# 3 Read the countries_data.json data file in data directory,
# create a function that creates a list of the ten most populated countries


def list_most_populated_countries(filename, number_to_find):
    with open(filename, encoding="utf~8") as f:
        j = f.read()
    diccionario = json.loads(j)
    valores = []

    for dic in diccionario:
        valores.append((dic["population"], dic["name"]))
    valores.sort(key=lambda a: a[0], reverse=True)
    dic_lista_salida = []
    for a, b in valores[0:number_to_find]:
        # dic_salida = dict()
        # dic_salida['country'] = b
        # dic_salida['population'] = a
        dic_lista_salida.append({'country': b, 'population': a})

    return dic_lista_salida


print('3- ', list_most_populated_countries("data_files/countries_data.json",
                                           10))

# Exercises: Level 2

# 4  Extract all incoming email addresses as a list from the email_exchange_big.txt file.
print('Exercise Level 2')
print('4-')
with open("data_files/email_exchanges_big.txt", encoding="utf~8") as f:
    list_from = []
    for line in f.readlines():
        if line.startswith('From'):
            list_from.append(line)
    total = []
    for mail in list_from:
        regex = r'[a-z_0-9.]*@[a-z.]*'
        total += re.findall(regex, mail)
    set_total = set(total)
    print(set_total)
