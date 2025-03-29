# # # # #   DICCIONARIOS    # # # # # #


# 1 Create an empty dictionary called dog

print()
dog = dict() 

# 2 Add name, color, breed, legs, age to the dog dictionary

dog = {
    'name': 'loli',
    'color': 'verde',
    'breed': 'calle',
    'legs': 3,
    'age': 32
}

# 3 Create a student dictionary and add first_name, last_name,
#   gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dict = {}
student_dict = student_dict.fromkeys([
    'first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills',
    'country', 'city', 'addres'
])
student_dict['skills'] = []
print(student_dict)

# 4 Get the length of the student dictionary
print("El largo del dic es:  ", len(student_dict))

# 5 Get the value of skills and check the data type, it should be a list
print(student_dict.get('skills'))
print("Tipo de dato del valor de la key skills:  ", type(student_dict.get('skills')))

# 6 Modify the skills values by adding one or two skills
student_dict['skills'] = ["alf", "polo"]

# 7 Get the dictionary keys as a list
print("Lista de las keys del dic:  ", list(student_dict.keys()))
print(type(list(student_dict.keys())))

# 8 Get the dictionary values as a list
print("Lista de los valores del dic:  ", list(student_dict.values()))

# 9 Change the dictionary to a list of tuples using items() method
tup_dict = student_dict.items()
tup_dict = list(tup_dict)
print("Lista de elementos en tuplas del dic")
print(tup_dict)
print("Tipo de la lista de tuplas:  ", type(tup_dict))

# 10 Delete one of the items in the dictionary
del student_dict['skills']
print(student_dict)

# 11 Delete one of the dictionaries

del dog

print(dog) # NameError: name 'dog' is not defined
