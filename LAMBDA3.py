# Python program performing 
# operation using def()
def fun(x, y, z):
    return x*y+z
a = 1
b = 2
c = 3

# logical jump 
d = fun(a, b, c)
print(d)

# Pythonn performing 
# operation using lambda 

d = (lambda x, y, z: x*y+z)(1, 2, 3)
print(d)
