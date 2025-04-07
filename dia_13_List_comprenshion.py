# # # # # # # #      List Comprenshion    # # # # # 

print()

#  1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

only_negative = [n for n in numbers if n <= 0]
print('1- ', only_negative)

# 2 Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat = [
    number for fila1 in list_of_lists for fila2 in fila1 for number in fila2
]
print('2- ', flat)

# 3  Using list comprehension create the following list of tuples:

list_tupla = [(j, j**0, j**1, j**2, j**3, j**4, j**5) for j in range(11)]
# f string genera la tupla como string asi join la junta ds de cada salto de linea

print('3- ')
print(list_tupla)

# 4 Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

list_pais = [[tupla[0].upper(), tupla[0][0:3].upper(), tupla[1].upper()]
             for i in countries for tupla in i]
print('4- ', list_pais)

# 5  Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

list_diccionary = [{
    'country': country.upper(),
    'city': city.upper()
} for row in countries for country, city in row]
print('5- ', list_diccionary)

# 6 Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

list_string = [name + ' ' + surname for row in names for name, surname in row]
print('6- ', list_string)

# 7
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.
print('7- lambda')
suma_15 = lambda a: a + 15
print(suma_15(5))
x_por_y = lambda x, y: x * y
print(x_por_y(6, 8))
