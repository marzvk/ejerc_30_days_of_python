###  LISTAS  ###

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

# nivel 1 --- ejercicio 1
#  Declare an empty list
list = []
# 2 Declare a list with more than 5 items
list = ['julio', 'agosto', 'mayo', 'enero', 'marzo', 'febrero']
# 3 Find the length of your list
print(len(list))
# 4 Get the first item, the middle item and the last item of the list
# print(list[::2]) se cumple en una lista de 5 elemenros
# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['jon', '71', '1.80', 'single', 'australia']
# 6 Declare a list variable named it_companies and assign initial values
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = [
    'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
]
# 7 Print the list using print()
print(it_companies)
# 8 Print the number of companies in the list
print(len(it_companies))
# 9 Print the first, middle and last company
print(it_companies[::3])
# 10 Print the list after modifying one of the companies
it_companies[0] = "Huawey"
print(it_companies)
# 11 Add an IT company to it_companies
it_companies.append("Logitech")
print(it_companies)
# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, "lumil")
print(it_companies)
# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = "HUAWEY"
print(it_companies)
# 14 Join the it_companies with a string '#;  '
strong = ['#; ']
print(it_companies + strong)
# 15 Check if a certain company exists in the it_companies list.
esta = "Google" in it_companies
print(esta)
# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18 Slice out the first 3 companies from the list
print(it_companies[3:])
# 19 Slice out the last 3 companies from the list
print(it_companies[0:-3])
# 20 Slice out the middle IT company or companies from the list
out = it_companies[2:4]
print(out)
print(it_companies)
# 21 Remove the first IT company from the list
it_companies.remove("lumil")
print(it_companies)
# 22 Remove the middle IT company or companies from the list
del it_companies[3]
print(it_companies)
it_companies.pop(3)
print(it_companies)
# 23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
# 27 After joining the lists in question 26. Copy the joined list and assign it
# to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
