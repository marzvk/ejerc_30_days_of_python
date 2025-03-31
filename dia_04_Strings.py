# # # # # # # STRINGS # # # # # #

print()
# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string,
# 'Thirty Days Of Python'.
print('1- ', "Thirty" + " " + "Days" + " " + "of" + " " + "Python")

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('2- ', "Coding" + " " + "for" + " " + "All")

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
COMPANY = "Coding for All"

# 4 Print the variable company using print().
print('4- ', COMPANY)

# 5 Print the length of the company string using len() method and print().
print('5- len:  ',len(COMPANY))

# 6 Change all the characters to uppercase letters using upper() method.
print('6- upper: ', COMPANY.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print('7- lower: ', COMPANY.lower())
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('8- capitalize: ', COMPANY.capitalize())
print('8- title: ', COMPANY.title())  # Coding For All
print('8- swapcase:  ', COMPANY.swapcase())  #cODING FOR aLL

# 9 Cut(slice) out the first word of Coding For All string.
print('9- slice: ', COMPANY[6::])

# 10 Check if Coding For All string contains a word Coding using the method
# index, find or other methods.
print('10- index: ', COMPANY.index("Coding"))
WORD = "Coding"
print('10- rindex: ', COMPANY.rindex(WORD))
print('10- startswith: ', COMPANY.startswith("Coding"))

# 11 Replace the word coding in the string 'Coding For All' to Python.
print('11- ', COMPANY.replace("Coding", "Python"))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
print('12- ', COMPANY.replace("Coding for All", "Python for Everyone"))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
COMPANY1 = 'Coding For All'
print('13- split: ', COMPANY1.split(" "))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
redes = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('14- split: ', redes.split(","))

# 15 What is the character at index 0 in the string Coding For All.
print('15- ', COMPANY[0])
# 16 What is the last index of the string Coding For All.
print('16- ', COMPANY[-1])
# 17 What character is at index 10 in "Coding For All" string.
print('17- ', COMPANY[10])  # es un espacio

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('18- ', "PFE")
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
print('19- ', 'CFO')

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
code = "Coding For All People"
print('20- ', code.index("C"))
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print('21- ', code.index("F"))
# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('22- ', code.rindex("l"))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ejem = 'You cannot end a sentence with because because because is a conjunction'
print('23- index: ', ejem.index("because"))

# 24 Use rindex to find the position of the last occurrence of the word because in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('24- rfind: ', ejem.rfind("because"))
# 25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('25- slice: ', ejem[31:54])
# 26 Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('26- ', ejem.find("because"))
# 27 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('27- ',ejem[0:30], ejem[55::])

# 28 Does ''Coding For All' start with a substring Coding?
variable = 'Coding For All'
print('28- startswith: ', variable.startswith("Coding"))

# 29 Does 'Coding For All' end with a substring coding?
print('29- endswith: ', variable.endswith("Coding"))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string
var = '   Coding For All      '
print('30- ', var)
new_var = var[3:18]
print('30- ', new_var)

# 31 Which one of the following variables return True when we use the method isidentifier():

var2 = '30DaysOfPython'
var3 = 'thirty_days_of_python'
print('31- ', var2.isidentifier())
print('31- ', var3.isidentifier())

# 32 The following list contains the names of some of python libraries:
lista_py = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#  Join the list with a hash with space string
nueva_lista = " # ".join(lista_py)
print('32- ', nueva_lista)

# 33 Use the new line escape sequence to separate the following sentences.
print('33- ', 'I am enjoying this challenge.\nI just wonder what is next.')

# 34 Use a tab escape sequence to write the following lines.
print('34 - ')
print('Name\t  Age \tCountry   City')
print('Asabeneh  250\tFinland   Helsinki')

# # 35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with a radius {} is {} meters square.'.format(radius, area)
# formated_string = 'The area of a circle with a radius %d is %d meters square.' %(radius, area)
print('35- ', formated_string)

# # 36 Make the following using string formatting methods:
a = 8
b = 6

print('36- ')
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')