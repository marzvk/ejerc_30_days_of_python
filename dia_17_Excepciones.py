# # # # # #      EXCEPCIONES   # # # # # #

print()
print('Exercises')
print()

print('1-')
try:
    print(10 + '5')
except:
    print('Something went wrong')

print('2-')
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2024 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

print('3-')
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2024 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print('Exception: ', e)

print('4- **kwargs')
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
        print(type(kwargs))
    return kwargs


print(
    packing_person_info(name="Asabeneh",
                        country="Finland",
                        city="Helsinki",
                        age=250))


print('5- *list')
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 8, 7, 11]
print(sum_of_five_nums(*lst))  # desempaca la lista

print('6- uso de enumerate: ')
for index, item in enumerate([20, 30, 40]):
    print(index, item)

print('7-')
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    print(f'The country {i} has been found at index {index}')

print('8- uso de zip: ')
#### ZIP ####
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)

print()
# Exercise

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# Unpack the first five countries and store them in a variable nordic_countries, 
# store Estonia and Russia in es, and ru respectively.

*nordic_countries, es , ru = names
print(nordic_countries)
print(es)
print(ru)
