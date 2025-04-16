# # # # # # # # EXPRESIONES REGULARES ## # # # # # # # #

import re

print()
print('Exercises: Level 1')
print()

# 1  What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

matches = re.sub(r'\.', '', paragraph)
print('1- ', matches)

matches = re.split(' ', matches)
print(matches)

match_set = set(matches)
print('set de unicas palabras: ', match_set)

lista = []
for palabra in match_set:
    lista.append(((matches.count(palabra)), palabra))
lista = sorted(lista, key=lambda a: a[0], reverse=True)

print('>>  Total  <<  ', lista)

print()
print('2-')
# 2
texto = 'The position of some particles on the horizontal x-axis are - 45 ,-12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20

regex = r'-?\d+'
points = re.findall(regex, texto)
enteros = list(map(int, points))
sorted_points = sorted(enteros)
print('Sorted points: ', sorted_points)
print(f'Distance = {sorted_points[-1]-sorted_points[0]}')

# # # # # # LEVEL 2 # # # # # #
print()
print('Exercises: Level 2')
print()
# Write a pattern which identifies if a string is a valid python variable

#regex_1 = r'\D[a-z_].[A-Z_a-z_0-9]'


def is_valid_variable(param):
    regex_1 = r'[a-zA-Z_][A-Z_a-z0-9]*$'
    if re.match(regex_1, param):
        print(True)
    else:
        print(False)


is_valid_variable('first_name')
is_valid_variable('first-name')  # False
is_valid_variable('1first_name')  # False
is_valid_variable('firstname')  # True


print()
print('Exercises: Level 3')
print()

# Clean the following text. After cleaning, count three most frequent words in the string

sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'


#coincide = re.sub(r'\$|%|@|&|#', '', sentence)

def clean_text(param):
    coincide = re.sub(r'[$%&#;.?@,!]', '', param)
    return coincide


print(clean_text(sentence))

def most_frequent_words(param1,number):
    matches = re.split(' ', param1)
    match_set = set(matches)
    lista = []
    for palabra in match_set:
        lista.append(((matches.count(palabra)), palabra))
    lista = sorted(lista, key=lambda a: a[0], reverse=True)
    return lista[0:number]


print(most_frequent_words(clean_text(sentence),10))
