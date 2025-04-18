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


# 5 Find the most common words in the English language

print('5-')


def clean_text(param):
    coincide = re.sub(r'[–$%&\n#;.?@,!-0-9]', "", param)
    coincide = re.sub(r'^\s+', "", coincide)
    coincide = re.sub('', "", coincide)
    return coincide


def find_most_comon_words(text, number):
    with open(text, encoding="utf~8") as f:
        txt = f.read()
    # txt_clean = re.sub(r'[–$%&#;.?@,!-]', '', txt)

    txt_clean = clean_text(txt)
    lista_palabras = re.split(' ', txt_clean)

    salida = []
    set_palabras = set(lista_palabras)
    for palabra in set_palabras:
        salida.append((lista_palabras.count(palabra), palabra))
    salida.sort(key=lambda a: a[0], reverse=True)
    return salida[0:number]


# 6
print('6- Donald speech: ',
      find_most_comon_words("data_files/donald_spech.txt", 10))

print('6- melina trump speech: ',
      find_most_comon_words("data_files/melina_trump_speech.txt", 10))

print('6- obama_speech: ',
      find_most_comon_words("data_files/obama_speech.txt", 10))

print('6- michelle obama: ',
      find_most_comon_words("data_files/michelle_obama_speech.txt", 10))

# 7 Write a python application that checks similarity between two texts


def remove_suport_words(param):
    with open(param, encoding="utf ~ 8") as f:
        j = f.read()
    # texto = re.sub(r'[–$%&#;.?@,!-]', '', j)
    texto = clean_text(j)
    lista_palabras = re.split(' ', texto)
    text_set = set(lista_palabras)
    lista_palabras_unicas = list(text_set)
    stop_words = [
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
        "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
        'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
        'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them',
        'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
        'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was',
        'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
        'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
        'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
        'about', 'against', 'between', 'into', 'through', 'during', 'before',
        'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
        'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
        'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
        'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
        'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
        'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
        'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',
        "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma',
        'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan',
        "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
        'won', "won't", 'wouldn', "wouldn't"
    ]
    for palabra in stop_words:
        if palabra in lista_palabras_unicas:
            lista_palabras_unicas.remove(palabra)
    # print(lista_palabras_unicas)
    print('lista palabras unicas: ', len(lista_palabras_unicas))
    print('len de stop words: ', len(stop_words))
    print('len de palabras limpias: ', len(text_set))


print('7-')
remove_suport_words("data_files/melina_trump_speech.txt")

# 8 Find the 10 most repeated words in the romeo_and_juliet.txt

print('8- ', find_most_comon_words("data_files/romeo_and_juliet.txt", 10))

# 9 read the hacker news csv file and find out:
#  a) Count the number of lines containing python or Python
#  b) Count the number lines containing JavaScript, javascript or Javascript
#  c) Count the number lines containing Java and not JavaScript

print('9-')
with open("data_files/hacker_news.csv") as f:
    csv_read = csv.reader(f)
    counter = 0
    for row in csv_read:
        archivo = ' '.join(row)
        # if 'python' in archivo or 'Python' in archivo:
        # if 'JavaScript' in archivo or 'javascript' in archivo or 'Javascript' in archivo:
        if 'Java' in archivo and 'JavaScript' not in archivo:
            counter += 1
    print(counter)

