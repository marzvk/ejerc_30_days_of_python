# Operadores

# 1 2 3

edad = 40
altura = 1.84
complejo = 1 + 2j  # numero complejo

# 4 calculo area triangulo

base = int(input("ingrese base triangulo: "))
altura_trian = int(input("ingrese altura del triangulo: "))
print(f'el area es : {0.5*base*altura_trian}')

# 5 calculo perimetro triangulo

lado_a = int(input("ingrese largo de lado a:"))
lado_b = int(input("ingrese largo lado b:"))
lado_c = int(input("ingrese largo lado c: "))
perimetro = print(f'El perimetro es: {lado_a + lado_b + lado_c}')

# 6 Obtenga el largo y el ancho de un rectángulo usando el mensaje.
#  Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))

largo = int(input("ingrese largo del rectangulo: "))
ancho = int(input("ingrese ancho del rectangulo: "))
print(f'el area del rectangulo es: {largo*ancho}')
print(f'el perimetro del rectangulo es: {2*(largo+ancho)}')

# 7 Obtenga el radio de un círculo usando el mensaje.
# Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.

PI = 3.14
radio = int(input("ingrese radio circulo: "))
print(f'el area del circulo es: {PI*radio*radio}')
print(f'la circunferencia es: {2*PI*radio}')

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
