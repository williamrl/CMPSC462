import array # importing array module

a = array.array('i', [1, 2, 3, 4, 5]) # creating an array of integers
print(a)
# d = array.array('d', [1.0, 2.1, 3.2, 4.3, 5.4]) # creating an array of double
# print(d)

# print(a[0]) # accessing the first element of the array
# print(a[:]) # slicing the array
# print(a[:-2]) # slicing the array

# a[0] = 10
# print(a) # changing the first element of the array
# a[:2] = array.array('i', [2, 4]) # changing the first two elements of the array
# print(a)

# a.append(6) # appending an element to the array
# print(a)
# a.extend([7, 8, 9]) # extending the array

b = array.array('i', [10, 11, 12])
c = array.array('i') # creating an empty array

c = a + b # concatenating two arrays
print(c)

del c[0] # deleting the first element of the array
print(c)
del c[0:2] # deleting the first two elements of the array
print(c)
# c.remove(6) # removing the element 6 from the array
print(c)
print(c.pop(4)) # removing the element at index of 4 in the array
print(c.pop()) # removing the last element of the array

c.insert(0, 0) # inserting 0 at the beginning of the array
print(a)