# to toatla numbers

import functools
numbers = [1,2,3,4,5,6,7,8,9]

calc = functools.reduce( lambda a ,b: a+b , numbers)

print(calc)
