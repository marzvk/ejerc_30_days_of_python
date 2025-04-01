# # # # # # #   CONDICIONALES   # # # # # # #

print()
print('Exercises Level 1')
print()

# Exercises: Level 1
# 1
print('# 1')
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print(f'Necesitas {18-edad} anios mas para manejar')
else:
    print('Tenes edad suficiente para aprender a manejar')

# 2
print('# 2')
MY_AGE = 29
your_age = int(input("Ingresa tu edad: "))
dif = MY_AGE  - your_age
if abs(dif) == 1 and MY_AGE  > your_age:
    print("Solo soy un anio mayor")
elif abs(dif) ==1 and MY_AGE  < your_age:
    print('Eres un anio mayor')
elif dif == 0:
    print("Mi edad es la misma que la tuya")
elif dif > 1:
    print(f'Yo soy {dif} anios mas viejo que tu')
else:
    print(f'Yo soy {abs(dif)} anios mas joven que tu')

# 3
print('# 3 - Comparar numeros: ')
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

if a > b:
    print(f'{a} es mayor que {b}')
elif a < b:
    print(f'{a} es menor que {b}')
else:
    print(f'{a} es igual que {b}') 


# level 2
print()
print("Exercises Level 2")
print()
print('# 1 Da nota de acuerdo a los scores: ')

score = int(input("Ingrese su nota (debe ser de 0 a 100):  "))

if score >= 90 and score <= 100:
    print("Su nota es A")
elif score >= 80 and score < 90:
    print("Su nota es B")
elif score >= 70 and score < 80:
    print("Su nota es C")
elif score >= 60 and score < 70:
    print("Su nota es D")
elif score >= 50 and score < 60:
    print("Su nota es E")
else:
    print("Su nota es F")  

# 2
print('# 2')
mes = input("Ingrese un mes del anio: ").lower()
verano = ["diciembre", "enero", "febrero"]
otonio = ["marzo", "abril", "mayo"]
invierno = ["junio", "julio", "agosto"]
primavera = ["setiembre", "octubre", "noviembre"]

if mes in verano:
    print("el mes ingresado esta en el verano")
elif mes in primavera:
    print("el mes ingresado esta en  primavera")
elif mes in invierno:
    print("el mes ingresado esta en el invierno")
elif mes in otonio:
    print("el mes ingresado esta en el otonio")
else : print('No ingreso un mes valido')

# 3
print('# 3')
fruits = ['banana', 'orange', 'mango', 'lemon', 'pera']
ingreso = input("ingrese una fruta: ").lower()

if ingreso in fruits:
    print("la fruta ya esta en la canasta")
else:
    fruits.append(ingreso)
    print(fruits)
                                       

# level 3
print()
print('Exercises: Level 3')
print()

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle
# skill in the skills list.

if person['skills']:
    middle = (len(person['skills']) // 2)
    print(' middle skills person: ', person['skills'][middle])

# Check if the person dictionary has skills key, if so check if the person has
# 'Python' skill and print out the result.

if person['skills']:
    if 'Python' in person['skills']:
        print('has ', 'Python')
    else:
        print('has ', 'no python')

# If a person skills has only JavaScript and React, print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#else print('unknown title') - for more accurate results more conditions can be nested!

if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'JavaScript' and 'React' in person['skills']:
    print('He is a front end developer')
else:
    print('unknown title')

# If the person is married and if he lives in Finland, print the information in the
#following format:

#Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred'] and 'Finland' in person['country']:
    print(f'{person['first_name']} {person["last_name"]} lives in {person['country']}. He is married')
