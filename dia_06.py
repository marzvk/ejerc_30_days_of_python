# # # # # TUPLAS # # # # #

# Exercises: Level 1

# 1   Create an empty tuple
# 2   Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 3   Join brothers and sisters tuples and assign it to siblings
# 4   How many siblings do you have?
# 5   Modify the siblings tuple and add the name of your father and mother and
#     assign it to family_members

print("Exercises Level 1")
names = tuple()
names = ("rigoberto", "ramon", "juan", "pedro")  # 2
print(type(names))
mas_nombres = tuple()
mas_nombres = ("yo", "tu", "ellos")  # 3
tupla_3 = names + mas_nombres
print(tupla_3)
print('El len de la tupla es: ',len(tupla_3)) # 4
padres = tuple()
padres = ("george", "jane") # 5
famyly_members = tupla_3 + padres
print("Los miembros de la familia son: \u2193 ")
print(famyly_members)
print(type(famyly_members))


#    Exercises: Level 2

# 1  Unpack siblings and parents from family_members

print("Exercises Level 2")
lista = list(famyly_members)
padres_list = lista[7:]
print("Los padres pasados en lista: ", padres_list)
mas_nombres_list = lista[4:7]
print("Elementos del 4 al 7: ",mas_nombres_list)
mas_nombres_nuevo = tuple(mas_nombres_list)
print(type(mas_nombres_nuevo))
nuevo_padres_tuple = tuple(padres_list)
print("Aqui como tupla: ",nuevo_padres_tuple)
print(type(nuevo_padres_tuple))

# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign
# it to a variable called food_stuff_tp.

fruits = ("manzana", "naranja")
vegetables = ("tomate", "apio")
animals_products = ("collar", "soga")

food_stuff_tp = fruits + vegetables + animals_products

print()
print(food_stuff_tp)
print(type(food_stuff_tp))

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
# 4  Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
out = food_stuff_lt[2:4]
print("slice en la parte central de la lista: ", out)
# 5  Slice out the first three items and the last three items from food_staff_lt list
print("Primeros tres elementos de la lista:", food_stuff_lt[0:3])
print("Ultimos tres elementos de la lista: ", food_stuff_lt[-3:])

# 6 Delete the food_staff_tp tuple completely

del food_stuff_tp
# print(food_stuff_tp)

# 7  Check if an item exists in tuple:

# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print(f'Estonia esta en los paises nordicos: {"Estonia" in nordic_countries}')
print(f'Islandia esta en los paises nordicos: {"Iceland" in nordic_countries}')
