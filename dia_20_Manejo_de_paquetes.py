import requests
import re
import json
import statistics
from collections import Counter
from bs4 import BeautifulSoup


# 1 Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

print('1-')
url = 'https://www.gutenberg.org/cache/epub/1777/pg1777.txt'
respuesta = requests.get(url, timeout=8)
txt = respuesta.text


def clean_text(param):
    coincide = re.sub(r'[–$%&\n#;.?@,!-0-9]', "", param)
    coincide = re.sub(r'^\s+', "", coincide)
    coincide = re.sub('', "", coincide)
    return coincide


def most_frequent_words(param1, number):
    matches = re.split(' ', param1)
    match_set = set(matches)
    lista = []
    for palabra in match_set:
        lista.append(((matches.count(palabra)), palabra))
    lista = sorted(lista, key=lambda a: a[0], reverse=True)
    return lista[0:number]


txt = clean_text(txt)

print(most_frequent_words(txt,10))


print('2-')
# 2  Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
print('i')
# i  the min, max, mean, median, standard deviation of cats' weight in metric units.

url = "https://api.thecatapi.com/v1/breeds"
respuesta_cat = requests.get(url)
cats = respuesta_cat.json()
peso_metric = []
for dic_cat in cats:
    for peso in dic_cat['weight']['metric']:
        peso_metric.append(peso)

valor = []
for i in peso_metric:
    if i.isnumeric():
        i = int(i)
        valor.append(i)

print('min: ', min(valor))
print('max: ', max(valor))

print('mean: ', statistics.mean(valor))
print('median: ', statistics.median(valor))
print('stdev: ', statistics.stdev(valor))


# ii the min, max, mean, median, standard deviation of cats' lifespan in years.

print('ii')
lifespan = []
for dics in cats:
    # for lifesp in dics['life_span']:
    #     lifespan.append(lifesp)
    lifespan.append(dics['life_span'].split())
# print(lifespan)  ['14', '-', '15']
numeros_life_span = []
for lista in lifespan:
    for number in lista:
        if number.isnumeric():
            number = int(number)
            numeros_life_span.append(number)

print('min: ', min(numeros_life_span),'.  max: ', max(numeros_life_span),
    '.  mean: ',  statistics.mean(numeros_life_span))
print('median life span: ', statistics.median(numeros_life_span))
print('stdev life span: ', statistics.stdev(numeros_life_span))



# iii  Create a frequency table of country and breed of cats

print('iii')

country = []
breed = []

for dics in cats:
    country.append(dics['origin'])
    breed.append(dics['name'])

x = Counter(country)
print(Counter(breed))

for i in x.keys():
    # print(i, ':', x[i])
    print(i, ':', (x[i] * '@'))


print('3-')
# 3 Read the countries API and find
print('i - the 10 largest countries:')
# i the 10 largest countries

url_3 = "https://restcountries.com/v3.1/all"
respuesta_pais = requests.get(url_3, timeout=8)
pais = respuesta_pais.json()

area = []
for dic in pais:
    area.append((dic['name']['common'], dic['area']))
area.sort(key=lambda a: a[1], reverse=True)
print(area[0:10])


print('ii - the 10 most spoken languages:')
# ii the 10 most spoken languages

language_list = []
for dic in pais:
    try:
        for lang in dic['languages'].values():
            language_list.append(lang)
    except:
        pass
    
idiom_set = set(language_list)

def most_spoken_languages(param):
    
    idiom_tuple = list()

    for idiom in idiom_set:
        idiom_tuple.append((idiom, language_list.count(idiom)))
    order = []
    for a in idiom_tuple:
        order = sorted(idiom_tuple, key=lambda a: a[1], reverse=True)
    return order[0:10]

print(most_spoken_languages(language_list))

# iii  the total number of languages in the countries API
print(f'iii - The total numbers of languages is :{len(idiom_set)}')

# 4  UCI is one of the most common places to get data sets for data science and machine learning. Read the 
# content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be
#  difficult, so you may try it with BeautifulSoup4

print('4-')

url_1 = 'https://oxylabs.io/blog/beautiful-soup-parsing-tutorial'
respuestas = requests.get(url_1, timeout=8)
content = respuestas.content  # contenido

soup = BeautifulSoup(content,'html.parser') # elementos
print(soup.title)
print(soup.title.get_text())

print('len h2: ', len(soup.h2.get_text()))
print(soup.h2)
print('li text: ', soup.li.text)
