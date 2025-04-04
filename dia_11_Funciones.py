# # # # # #    FUNCIONES    # # # # # #

print()
print("Exercises Level 1")
print()
# level 1
#1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.


def suma_dos_numeros(valor_1, valor_2):
    # suma dos numeros
    suma = valor_1 + valor_2
    return suma


print('1- ', suma_dos_numeros(7, 11))

# 2

# Area of a circle is calculated as follows: area = π x r x r. Write a function
# that calculates area_of_circle.


def area_de_circulo(radio):
    Pi = 3.14
    area = Pi * radio**2
    return area


print('2- ', area_de_circulo(8))

# 3
# Write a function called add_all_nums which takes arbitrary number of arguments
# and sums all the arguments. Check if all the list items are number types.
# If not do give a reasonable feedback.


def suma_todos_numeros(*numbers):
    total = 0
    for num in numbers:
        if type(num) != int:
            print(num, "no es entero, cambie ", num,
                  'y vuelva a iniciar la funcion')
            return

        total = total + num

    return total


print('3- ', suma_todos_numeros(1, 2, 3, 4, 5))

# 4
# Temperature in °C can be converted to °F using this formula:°F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, convert_celsius_to-fahrenheit


def convert_cels_a_farenh(celsius):
    farenheit = (celsius * 9 / 5) + 32
    return farenheit


print('4- ', convert_cels_a_farenh(32))

# 5
# Write a function called check-season, it takes a month parameter and returns
#  the season: Autumn, Winter, Spring or Summer.


def chek_season(mes):
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
    else:
        print("ingrese bien el mes")
    return


print('5- ')
chek_season('octav')

# 6 Write a function called calculate_slope which return the slope of a linear equation


def calculo_pendiente(x1, y1, x2, y2):
    pendiente = (y2 - y1) / (x2 - x1)
    return pendiente


print('6- ', calculo_pendiente(1, 3, 7, 5))

# 7
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function
# which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def ecuation_cuad(a, b, c, x):
    resultado = (a * (x**2)) + b * x + c
    return resultado


print('7- ', ecuation_cuad(2, 3, 5, 2))

# 8
# Declare a function named print_list. It takes a list as a parameter and
# it prints out each element of the list.


def print_list(param):
    for i in param:
        print(i)
    return


print('8- ')
print_list([1, 2, 7])

# 9
# Declare a function named reverse_list. It takes an array as a parameter and
# it returns the reverse of the array (use loops).


def lista_reversa(param):
    lista_inversa = []
    for i in range(len(param), 0, -1):
        lista_inversa.append(param[i - 1])  # len tiene 4.lista va de 0 a 3
    return lista_inversa


print('9- ', lista_reversa([1, 2, 3, 4, 5]), lista_reversa(['a', 'b', 'c']))

# 10 Declare a function named capitalize_list_items
# It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(param):
    capitalized = []
    for i in range(len(param)):
        capitalized.append((param[i]).capitalize())
    return capitalized


print('10- ', capitalize_list_items(['pepe', 'lolo']))

# 11
# Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.


def add_item(param1, param2):
    param1.append(param2)
    return param1


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('11- ', add_item(food_staff,
                       'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print('11- ', add_item(numbers, 5))  #[2, 3, 7, 9, 5]

# 12
# Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.


def remove_item(param1, param2):
    param1.remove(param2)
    return param1


print('12- ', remove_item(food_staff, 'Mango'))
print('12- ', remove_item(numbers, 3))

# 13
# Declare a function named sum_of_numbers. It takes a number parameter and it
# adds all the numbers in that range.


def sum_of_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum


print('13- ', sum_of_numbers(5))  # 15
print('13- ', sum_of_numbers(10))  # 55
print('13- ', sum_of_numbers(100))  # 5050

# 14
# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.

def suma_impares(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 != 0:
            sum = sum + i
    return sum
print('14- ', suma_impares(20))

# 15
# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that range.

def suma_pares(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum
print('15- ', suma_pares(20))

print()
print("Exercises Level 2")
print()
# LEVEL 2

# 1
# Declare a function named evens_and_odds . It takes a positive integer as 
# parameter and it counts number of evens and odds in the number.

def pares_e_impares(n):
    cuenta_par = 0
    cuenta_inpar = 0
    for i in range(n + 1):
        if i % 2 == 0:
            cuenta_par = cuenta_par + 1
        else:
            cuenta_inpar = cuenta_inpar + 1
    print(f'la cuenta de los pares es:  {cuenta_par}')
    print(f'la cuenta de los impares es: {cuenta_inpar}')
    return
print('1- ')
pares_e_impares(100)

# 2
# Call your function factorial, it takes a whole 
# number as a parameter and it return a factorial of the number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print('2- ', factorial(6))

# 3
# Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(param):
    if param:
        return False
    else:
        return True

print('3- ', is_empty(food_staff))

# 4
# Write different functions which take lists. They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

data = [2, 6, 4, 5, 5, 5, 4]
print()
print(data)

def calculo_media(param):
    sum_list = 0
    for i in param:
        sum_list = sum_list + i
    media = sum_list / len(param)
    return media
print('4- La media es: ', calculo_media(data))

def mediana(param):
    param.sort()
    media = len(param) // 2
    valor = param[media]
    return valor
print('4- La mediana es: ', mediana(data))

def moda(param):
    set_param = set(param)
    list_tuple = list()
    for i in set_param:
        list_tuple.append((param.count(i), i))
    moda = []
    moda = sorted(list_tuple, key=lambda a: a[0], reverse=True)
    return moda[0][1]

print('4- Moda: ', moda(data))

def rango(param):
    param = sorted(param)
    ran = param[-1] - param[0]
    #print(f'El valor del rango es: {ran}')
    return ran
print('4- El valor del rango es: ', rango(data) )

def varianza(param):
    mid = calculo_media(param)
    sumatoria = 0
    for i in param:
        sumatoria = sumatoria + (i - mid)**2
    var = sumatoria / len(param)
    return var
print('4- Varianza: ', varianza(data) )

def desviacion_std(param):
    wed = varianza(param)
    return wed**0.5
print('4- Std deriv', desviacion_std(data))

print()
print("Exercises Level 3")
print()

# LEVEL 3
# 1
# Write a function called is_prime, which checks if a number is prime.

def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print('1-   8 => Is prime? :', es_primo(8))

# 2 Write a functions which checks if all items are unique in the list

def chequeo_unico(param):
    list_set = set(param)
    if len(param) == len(list_set):
        print("Todos los elementos de la lista son unicos")
        return
    else:
        print("La lista tiene elementos repetidos")
    return
print('2-')
chequeo_unico(food_staff)

# 3 Write a function which checks if all the items of the list are of the same data type.

date = [2, 5, 4, 9, 5]

def chequeo_type(param):
    elem_type = type(param[0])
    for elem in param:
        if type(elem) != elem_type:
            return False
    return True
print('3-')
print("Los items de la lista son del mismo type: ", chequeo_type(date))

# 5 
# # 1  Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order

# Buscar en esa direccion el archivo
data = 'https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py'


def most_spoken_languages(param):
    idiomas = []
    idiom_set = set()

    for dic in param:
        for i in dic['languages']:
            idiomas.append(i)
            idiom_set.add(i)
    idiom_tuple = list()

    for idiom in idiom_set:
        idiom_tuple.append((idiom, idiomas.count(idiom)))
    order = []
    for _ in idiom_tuple:
        order = sorted(idiom_tuple, key=lambda a: a[1], reverse=True)
    return order[0:10]


# print(most_spoken_languages(data))


# 5
# # 2     Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.


def most_populated_countries(param):
    cantidades = []

    for dic in param:
        cantidades.append(((dic['name']), dic['population']))
    cantidades.sort(key=lambda a: a[1], reverse=True)
    return cantidades[0:20]


# print(most_populated_countries(data))
