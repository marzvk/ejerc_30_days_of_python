# # # # SETS # # #

it_companies = {
    'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
}

# Exercises: Level 1

# 1     Find the length of the set it_companies
# 2     Add 'Twitter' to it_companies
# 3     Insert multiple IT companies at once to the set it_companies
# 4     Remove one of the companies from the set it_companies
# 5     What is the difference between remove and discard

print()
print("Exercises Level 1")
print()

print("Set de it_companies: ", it_companies)
print("El len es:  ", (len(it_companies)))  # 1
it_companies.add("Twitter")  # 2
print("Agregamos twitter:  ", it_companies)
print("Update metodo para agregar ")
it_companies.update(["Huawei", "Lenovo", "Reddragon"])  # 3
print(it_companies)
it_companies.remove("Reddragon")  # 4
print("Remove reddragon:  ", it_companies)

it_companies.discard(
    "lolo")  # remueve el elemento si es un miembro, no arroja error
# si el elemento no existe

# it_companies.remove()
# remove arroja error si el elemnento no existe

# la diferencia es q .discard() no arroja error al intentar eliminar un elemento del conjunto
# aunque dicho elemento no se encuentre , es una manera mas segura de eliminar elementos

# Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print()
print("Exercises Level 2")
print()

# 1     Join A and B
# 2     Find A intersection B
# 3     Is A subset of B
# 4     Are A and B disjoint sets
# 5     Join A with B and B with A
# 6     What is the symmetric difference between A and B
# 7     Delete the sets completely

print("Conjunto A:  ", A)
print("Conjunto B:  ", B)
C = A.union(B)
print("Join A and B:  ", C)  # 1
print("A insterseccion con B:  ", A.intersection(B))  # 2
print("A issubset B:  ", A.issubset(B))  # 3 ,tienen elementos en comun o no
print("A disjoint B:  ", A.isdisjoint(B)) # 4
# coinciden en 24 por ejemplo,por lo tanto no son disjoint, es ser null intersection

A.update(B)
print("A union con B:  ", A)

B.union(A)
print("B union con A:  ", B)

print(A.symmetric_difference(B))  # {27 , 28} solo del set B son 

del A # 7 
del B


# Exersices level 3

print()
print("Exersices Level 3")
print()

age = [22, 19, 24, 25, 26, 24, 25, 24]

print("age : ", age)

# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 2 Explain the difference between the following data types: string, list, tuple and set
# 3 I am a teacher and I love to inspire and teach people.
#   How many unique words have been used in the sentence?
#   Use the split methods and set to get the unique words.

age_set = set(age)
print("type age:  " , type(age))
print("type age set:  ", type(age_set))
print("len set: ", len(age_set))
print("len lista age:  ", len(age))  
print("el len de la lista es mas largo porque acepta repetidos")

PALABRAS_STR = "I am a teacher and I love to inspire and teach people"
print(PALABRAS_STR)
nueva = PALABRAS_STR.split()
print("Split:", nueva)
print("type: ", type(nueva))
print("Len de la lista: ", len(nueva))
pala_set = set(nueva)
print("Como set: ", pala_set)
print("Len del set:  '", len(pala_set), "' la cantidad de palabras unicas.")  
