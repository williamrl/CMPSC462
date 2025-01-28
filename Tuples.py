x = (3, 5, 4, 6)
y = (1, 2)
x = list(x)
# print(x)
# x[0] = 10

for i in x:
    print(i)

# print(x + y)
# print (y**2) # Error because tuple does not support item assignment (IMMUTABLE)
# print(y[0] * 2)

x[1] = 3
x= tuple(x) # Convert list to tuple
print(x)

# print(x.index(8))
print(x.count(3))