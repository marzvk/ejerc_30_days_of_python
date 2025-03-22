# 30 days of python programing

first_name = "lucia"
last_name = "salinas"
full_name = "lucia salinas"
country = "brasil"
city = "porto alegre"
age = 94
year = 1988
is_married = True
is_true = "hapiness"

# 1 2 3

print(len(first_name)) # largo en caracteres, 5
print(len(last_name))
print(type(first_name)) # <class 'str'>
print(type(full_name))
print(type(age)) # int
print(type(is_married)) # bool
print(type(is_true))

#4

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(floor_division)
print(exp)
print(remainder)

#5
radius_circle = 30
pi = 3.14
area = pi * (radius_circle**2)
circunferencia_circulo = (2 * pi) * radius_circle
# ingreso es la entrada por pantalla
ingreso = int(input("ingrese radio del circulo: "))
print(f'el area del circulo es {3.14*(ingreso**2)}')
print(area)
print(circunferencia_circulo)
