# # # # # #   LISTAS  # # # # # # 


first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

countries = [
    'Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway',
    'Iceland', 'Estonia'
]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Exercises: Level 1

print()
print('Exercises: Level 1')
print()

# 1 Declare an empty list
empty_list = []

# 2 Declare a list with more than 5 items
lista = ['julio', 'agosto', 'mayo', 'enero', 'marzo', 'febrero']
print('2 - lista = ', lista)

# 3 Find the length of your list
print('3- len de lista: ', len(lista))

# 4 Get the first item, the middle item and the last item of the list
print('4 - middle item: ', lista[int(len(lista)/2)])
print(lista[::2])
# en una lista impar de 5 funciona

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['jon', '71', '1.80', 'single', 'australia']

# 6 Declare a list variable named it_companies and assign initial values
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = [
    'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
]

# 7 Print the list using print()
print('7- ', it_companies)

# 8 Print the number of companies in the list
print('8- len de la lista: ', len(it_companies))

# 9 Print the first, middle and last company
print('9- ', it_companies[::3])

# 10 Print the list after modifying one of the companies
it_companies[0] = "Huawey"
print('10 ', it_companies)

# 11 Add an IT company to it_companies
it_companies.append("Logitech")
print('11- append: ', it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, "lumil")
print('12- insert: ', it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = "HUAWEY"
print('13- ', it_companies)

# 14 Join the it_companies with a string '#;  '
strong = ['#; ']
print('14 ', it_companies + strong)

# 15 Check if a certain company exists in the it_companies list.
existe = "Google" in it_companies
print('15- ', existe)

# 16 Sort the list using sort() method
it_companies.sort()
print('16- sort: ', it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print('17- reverse: ', it_companies)

# 18 Slice out the first 3 companies from the list
print('18- ', it_companies[3:])

# 19 Slice out the last 3 companies from the list
print('19- ', it_companies[0:-3])

# 20 Slice out the middle IT company or companies from the list
out = it_companies[2:4]
print('20- ', out)
print('20- ', it_companies)

# 21 Remove the first IT company from the list
it_companies.remove("lumil")
print('21- ', it_companies)

# 22 Remove the middle IT company or companies from the list
del it_companies[3]
print('22- del: ', it_companies)

it_companies.pop(3)
print('22- pop: ', it_companies)

# 23 Remove the last IT company from the list
it_companies.pop()
print('23- pop: ', it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print('24- clear: ', it_companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print('26- join lists: ', full_stack)

# 27 After joining the lists in question 26. Copy the joined list and assign it
# to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print('27- insert: ', full_stack)



#  # # # Exercises: Level 2   # # # # #

print()
print('Exercises Level 2')
print()

#   1 The following is a list of 10 students ages:
print(' # 1')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print('sort: ', ages)
ages.append(19)
ages.append(26)
ages.sort()
print(ages)

average = (sum(ages) / len(ages))  # average age
range_ages = max(ages) - min(ages)
print('average: ', average)
print('range ages: ', range_ages)
print('abs de min - average:  ', abs(min(ages) - average))
print('abs de max - average:  ', abs(max(ages) - average))

#Sort the list and find the min and max age
#Add the min age and the max age again to the list
#Find the median age (one middle item or two middle items divided by two) 24
#Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method

# 2 
print('# 2')

#Find the middle country(ies) in the countries list
print('middle country of list: ', len(countries) / 2)

#Divide the countries list into two equal lists if it is even if not one
#  more country for the first half.

# lista en :
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py

print(countries[96:98])
lista_1 = countries[0:98]
lista_2 = countries[98::]

# 3 

print('# 3 ')
otros_paises = [
    'China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'
]
ch, rus, usa, *scandic = otros_paises
print(ch)
print(rus)
print('Scandic: ' , scandic)
# Unpack the first three countries and the rest as scandic countries.
