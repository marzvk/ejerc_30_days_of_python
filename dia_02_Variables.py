# Variables

# Exercises Level 1

# 30 days of python programing    # 2

first_name = "lucia"  # 3
last_name = "salinas" # 4
full_name = "lucia salinas" # 5
country = "brasil" # 6
city = "porto alegre" # 7
age = 94 # 8
year = 1988 # 9
is_married = True # 10
is_true = "hapiness" # 11
is_light_on = True # 12
peso, edad, altura = 91, 40, 'desconocida' # 13


# Exercises Level 2

# 1 Check the data type of all your variables using type() built-in function
# 2 Using the len() built-in function, find the length of your first name
# 3 Compare the length of your first name and your last name

print(len(first_name)) # largo en caracteres, 5
print(len(last_name))
print(type(first_name)) # <class 'str'>
print(type(full_name))
print(type(age)) # int
print(type(is_married)) # bool
print(type(is_true))

# 4 Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

# 5 Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# 6 Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# 7 Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# 8 Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 9 Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two

# 10 Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# 11 Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

print("floor division:  ", floor_division)
print("exp:  ",exp)
print("remanider:  ", remainder)

# 12 The radius of a circle is 30 meters.
# i -Calculate the area of a circle and assign the value to a variable name of area_of_circle
# ii-Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# iii-Take radius as user input and calculate the area.

radius_circle = 30
pi = 3.14
area = pi * (radius_circle**2)
circunferencia_circulo = (2 * pi) * radius_circle
# ingreso es la entrada por pantalla
ingreso = int(input("Ingrese radio del circulo: "))
print(f'El area del circulo es {3.14*(ingreso**2)}')
print(area)
print(circunferencia_circulo)

# 13 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print()
print("Welcome USer: ")
primer_nombre = input("ingrese el first_name: ")
apellido = input("Ingrese el last_name: ")
pais = input("Ingrese su country:  ")
anios = input("Ingrese su edad:  ")

