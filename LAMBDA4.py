def func(x):
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    else: 
        return "ten"
num = func(3)
print(num)

# Python program showing use 
# of lambda function 
num = (lambda x: "one" if x == 1 else("two" if x == 2 else ("three" if x == 3 else "ten")))(3)
print(num)
