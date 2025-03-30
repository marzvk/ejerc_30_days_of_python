# # # # # # # Operadores  # # # # # # # #

print()

# 1 Declare your age as integer variable
# 2 Declare your height as a float variable
# 3 Declare a variable that store a complex number

edad = 40
altura = 1.84
complejo = 1 + 2j  # numero complejo

# 4 calculo area triangulo

base = int(input("Ingrese base triangulo: "))
altura_trian = int(input("Ingrese altura del triangulo: "))
print(f'El area del triangulo es : {0.5*base*altura_trian}')

# 5 calculo perimetro triangulo

lado_a = int(input("Ingrese largo de lado a:"))
lado_b = int(input("Ingrese largo lado b:"))
lado_c = int(input("Ingrese largo lado c: "))
perimetro = print(f'El perimetro del triangulo es: {lado_a + lado_b + lado_c}')

# 6 Obtenga el largo y el ancho de un rectángulo usando el mensaje.
#  Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))

largo = int(input("Ingrese largo del rectangulo: "))
ancho = int(input("Ingrese ancho del rectangulo: "))
print(f'El area del rectangulo es: {largo*ancho}')
print(f'El perimetro del rectangulo es: {2*(largo+ancho)}')

# 7 Obtenga el radio de un círculo usando el mensaje.
# Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.

PI = 3.14
radio = int(input("Ingrese radio circulo: "))
print(f'El area del circulo es: {PI*radio*radio}')
print(f'La circunferencia del circulo es: {2*PI*radio}')

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

print(
    "si x es igual a cero, intercepta a y en: y = 2(0)-2, eso da -2. el punto es(0,-2) "
)
print(("si y es igual a cero, 0 = 2x -2, eso da x = 1. el punto es : (1,0)"))
m = (0 - (-2)) / (1 - 0)
print(m)

# 9 Slope is (m = y2-y1/x2-x1).
#  Find the slope and Euclidean distance between point (2, 2) and point (6,10)

m = (10 - 2) / (6 - 2)
print(m)

# dist euclid = (x2-x1)**2 + (y2-y1)**2

distance_euclidiana = (4)**2 + (8)**2
print(distance_euclidiana)

# 10 compare las dos pendientes anteriores
# las pendientes son iguales

# 11 Calculate the value of y (y = x^2 + 6x + 9).
#  Try to use different x values and figure out at what x value y is going to be 0

x = int(input("Ingrese valor de x: "))
print(f' y = {x**2 + 6*x +9}')
# - 3 en x da 0 de resultado en y

# 12  Find the length of 'python' and 'dragon' and make a falsy comparison statement

print("El len de 'python' es:  ", len("python"))
print("El len de 'dragon' es:  ", len("dragon"))

print("El len de python != dragon:  " ,len("python") != len("dragon"))  # False

# 13  Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("13", 'on' in 'python' and 'on' in 'dragon')

# 14 I hope this course is not full of jargon. Use in operator to check if jargon
# is in the sentence.
print("14", "jargon" in "I hope this course is not full of jargon")

# 15 There is no 'on' in both dragon and python
print("15", 'on' not in 'python' and 'on' in 'dragon')

# 16 find the length of the text python and convert the value to float and convert it to string
print("16 => type(str(float(len(python))))):  ", type(str(float(len("python")))))

# 17 Even numbers are divisible by 2 and the remainder is zero.
#     How do you check if a number is even or not using python?
# num % num == 0 is ok

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("18 >>> (7//3 == int(2.7)) =>  ", 7//3 == int(2.7))

# 19 Check if type of '10' is equal to type of 10
print("19 >>> type('10') == type(10) =>  ",type('10') == type(10)) # False

# 20 Check if int('9.8') is equal to 10
print("20 >>> (int(9.8) == 10) =>  ",int(9.8) == 10)

# 21     Writ a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?

horas = float(input("Ingrese horas trabajadas: "))
ingreso = float(input("Ingrese ganancia por hora: "))
print(f"Su ingreso semanal es: {ingreso*horas}")

# 22 Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
edad = int(input("Ingrese los anios vividos: "))
print(f'Usted ha vivido {edad*31536000} segundos')

# 23 Write a Python script that displays the following table
print(
    "1\t1\t1\t1\t1\n2\t1\t2\t4\t8\n3\t1\t3\t9\t27\n4\t1\t4\t16\t64\n5\t1\t5\t25\t125"
)
