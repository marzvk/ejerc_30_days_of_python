# # # # # # # # #    Modulos   ; ; ; ; ; ; ; ; ;

import string
import random
import os
print(os.getcwd()) # mostrar directorio actual

print()
print("   Exercises Level 1")
print()
# ejercicio level 1

#  1
# Writ a function which generates a six digit/character random_user_id.

todo = string.ascii_letters + string.digits


def random_user_id():
    res = []
    for _ in range(6):
        res.append(todo[random.randint(0, len(todo) - 1)])
        # genera un valor random de las letras tomadas en todo
    resul = ''.join(res)
    resul = f"'{resul}'"
    return resul


print("1- ", random_user_id())  #'1ee33d'

# 2
# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is
# the number of IDs which are supposed to be generated.


def user_id_gen_by_user():
    total = []
    cantidad = int(input("Cantidad de Id a generar: "))
    largo = int(input("Cantidad de caracteres: "))

    for _ in range(cantidad):

        res = []
        for _ in range(largo):
            res.append(todo[random.randint(0, len(todo) - 1)])
        Resul = ''.join(res)
        total += f"{Resul}\n"
    return ''.join(total)

print("2- ")
print( user_id_gen_by_user())

# 3
# Write a function named rgb_color_gen. It will generate rgb colors
# (3 values ranging from 0 to 255 each).


def list_rgb_colors(cantidad):
    total = []

    for _ in range(cantidad):
        rgb_color = []
        for _ in range(3):
            rgb_color.append(random.randint(0, 255))
        total.append(
            f"rgb({rgb_color[0]:03d},{rgb_color[1]:03d},{rgb_color[2]:03d})")
    return total


print("3- ", list_rgb_colors(5))

print()
print("   Exercises Level 2")
print()

# level 2   

# 1 Write a function list_of_hexa_colors which returns any number of hexadecimal 
# colors in an array (six hexadecimal numbers written after #. Hexadecimal 
# numeral system is made out of 16 symbols, 0-9 and first 6 letters of the 
# alphabet, a-f. Check the task 6 for output examples).

from string import hexdigits


def list_of_hexa_colors(cantidad):
    hexa = hexdigits[0:16]

    total = []
    for _ in range(cantidad):
        color_hexa = []
        for _ in range(6):
            color_hexa.append(hexa[random.randint(0, len(hexa) - 1)])
        number = '#' + ''.join(color_hexa) # se le da un string vacio a join al inicio
        total.append(number)
    return total


print('1- ', list_of_hexa_colors(4))

# 2
# antes esta resuelta mas arriba

# 3 Write a function generate_colors which can generate any number of hexa or rgb colors.


def generate_colors(ponga_clase, ponga_cantidad):

    if ponga_clase == 'rgb':

        return list_rgb_colors(ponga_cantidad)

    elif ponga_clase == 'hexa':

        return list_of_hexa_colors(ponga_cantidad)
    else:
        return 'clase error'


print('3- ', generate_colors('rgb', 5))

print()
print('   Exercises Level 3')
print()

# Level 3
# 1 Call your function shuffle_list, it takes a list as a parameter
#  and it returns a shuffled list

muestra = [2, 3, 4, 5, 6, 7, 8, 9, 55, 4, 12, 16, 18, 19, 15, 14, 15]


def shufle_list(param):
    shufle = []
    for _ in range(len(param)):
        shufle.append(param.pop(random.randint(0, len(param) - 1)))
    return shufle

print(muestra)
print('1- ', shufle_list(muestra))

# 2 Write a function which returns an array of seven random numbers 
# in a range of 0-9. All the numbers must be unique.


def rand_num_7():
    set_num = set()

    while len(set_num) < 7:
        set_num.add(random.randint(0, 9))
    s = list(set_num)
    return s


print('2- ', rand_num_7())
print()
numbers = [(i, i * i) for i in range(11)]
print('i, i * i :', numbers)