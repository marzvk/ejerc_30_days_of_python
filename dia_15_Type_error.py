# # # # # # # #    Type error     # # # # # # # # #
print()
print('Type errors')
print()


print(e)
# NameError: name 'e' is not defined

print'hello world'
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

numeros = [1, 2, 3]
numeros[4]
# IndexError: list index out of range

import maths
# No encuentra el modulo porque tiene una s de mas
# ModuleNotFoundError: No module named 'maths'

import math
math.PI
# mal escrita la llamada al modulo
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

user = {'name':'Franklin', 'edad': 1420, 'planet': 'Mars'}
user['planet']
user['galaxia']
# KeyError: 'galaxia'

4+'3'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

from math import potencia
# ImportError: cannot import name 'potencia' from 'math' (unknown location)

int('2j')
# ValueError: invalid literal for int() with base 10: '2j'

1/0
#     1/0
#     ~^~
# ZeroDivisionError: division by zero