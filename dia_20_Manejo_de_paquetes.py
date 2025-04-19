import requests
import re
import json
import statistics


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
