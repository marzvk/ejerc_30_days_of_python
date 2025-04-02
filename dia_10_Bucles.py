# # # # #       BUCLES      # # # # #

print()
print("Exercises Level 1")
print()
# Exercises Level 1


# 1

print("1 - ")
for i in range(1,11):
    print(i)
num = 0
while num < 10:
    num += 1
    print( num) 

# 2

print("2 -")
for i in range(10, -1, -1):
    print(i)

num = 11
while num > 0:
    num -= 1
    print(num)

# 3

print("3 -")
for i in range(7):
    i += 1
    print('#'*i)

# 4  

print("4 -")
for i in range(8):
    for j in range(8):
        print('#', end=" ")
    print()

# 5

print("5 -")
for i in range(11):
    print(i,'x',i,'=',i*i) 

# 6

print('6 -')
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in lista:
    print(i)  

# 7 # 8

print('7 -')
for i in range(1, 101):  # numeros pares
    if i % 2 == 0:
        print(i)

print('8 -')
for i in range(1, 100): # numeros impares
    if i % 2 != 0:
        print(i)  

# LEVEL 2
print()
print('Exercises Level 2')
print()
# 1

print('1 -')
suma = 0
for i in range(101):
    suma += i
print('La suma de todos los numeros del 1 al 100 es: ', suma)

# 2

print('2 - ')
sum_par = 0
sum_imp = 0
for i in range(101):
    if i % 2 != 0:
        sum_imp += i
    else:
        sum_par += i
print("La suma de todos los impares hasta el 100 es: ", sum_imp)
print("La suma de todos los pares hasta el 100 es: ", sum_par)

# Exercises Level 3
print()
print('Exercises Level 3')
print()

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

# 1

print('1 -')

for i in countries:
    if i.find("land") > 0:  # find da -1 si no encuentra nada que cooincida con lo requerido
        print(i)

# 2

print('2 -')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []
for i in range(len(fruits), 0, -1):  
    # el len arranca de 4 a 1, por eso se imprime - 1 ,
    fruits_reverse.append(fruits[ i - 1 ]) 
     # porq fruits arranca de 0 a 3. y recorrido alreves no coincide

print(fruits)
print('Lista al reves: ', fruits_reverse)
print(type(fruits_reverse))
