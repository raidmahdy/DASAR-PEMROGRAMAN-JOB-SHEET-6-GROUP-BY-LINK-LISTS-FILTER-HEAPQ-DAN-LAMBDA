# Python code to ilustrate 
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
sum = reduce((lambda x, y: x + y), li)
print(sum)
