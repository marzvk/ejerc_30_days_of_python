# STRINGS

# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string,
# 'Thirty Days Of Python'.
print("Thirty" + " " + "Days" + " " + "of" + " " + "Python")

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding" + " " + "for" + " " + "All")

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
# 4 Print the variable company using print().
# 5 Print the length of the company string using len() method and print().
# 6 Change all the characters to uppercase letters using upper() method.
# 7 Change all the characters to lowercase letters using lower() method.
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# 9 Cut(slice) out the first word of Coding For All string.

COMPANY = "Coding" + " " + "for" + " " + "All"
print(COMPANY)  # 14
print(len(COMPANY))
print(COMPANY.upper())
print(COMPANY.lower())
print(COMPANY.capitalize())
print(COMPANY.title())  # Coding For All
print(COMPANY.swapcase())  #cODING FOR aLL
print(COMPANY[6::])

# 10 Check if Coding For All string contains a word Coding using the method
# index, find or other methods.

# 11 Replace the word coding in the string 'Coding For All' to Python.
# 12 Change Python for Everyone to Python for All using the replace method or other methods.

COMPANY = "Coding" + " " + "for" + " " + "All"
WORD = "Coding"
print(COMPANY.index("Coding"))
print(COMPANY.rindex(WORD))
print(COMPANY.startswith("Coding"))
print(COMPANY.replace("Coding", "Python"))
print(COMPANY.replace("Coding for All", "Python for Everyone"))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
COMPANY1 = 'Coding For All'
print(COMPANY1.split(" "))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
redes = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(redes.split(","))

# 15 What is the character at index 0 in the string Coding For All.
# 16 What is the last index of the string Coding For All.
# 17 What character is at index 10 in "Coding For All" string.

# COMPANY = ("Coding" + " " + "for" + " " + "All")
print(COMPANY)
print(COMPANY[0])
print(COMPANY[-1])
print(COMPANY[10])  # es un espacio

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

code = "Coding For All People"
print(code.index("C"))
print(code.index("F"))
print(code.rindex("l"))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# 24 Use rindex to find the position of the last occurrence of the word because in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'

# 25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

# 26 Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

# 27 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

ejem = 'You cannot end a sentence with because because because is a conjunction'
print(ejem.index("because"))
print(ejem.rfind("because"))
print(ejem[31:54])
print(ejem.find("because"))

# 28 Does ''Coding For All' start with a substring Coding?
# 29 Does 'Coding For All' end with a substring coding?

variable = 'Coding For All'
print(variable.startswith("Coding"))
print(variable.endswith("Coding"))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string

var = '   Coding For All      '
print(var)
new_var = var[3:18]
print(new_var)

# 31 Which one of the following variables return True when we use the method isidentifier():

var2 = '30DaysOfPython'
var3 = 'thirty_days_of_python'
print(var2.isidentifier())
print(var3.isidentifier())

# 32 The following list contains the names of some of python libraries:

lista_py = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

#  Join the list with a hash with space string

nueva_lista = " # ".join(lista_py)
print(nueva_lista)
