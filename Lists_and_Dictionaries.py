# #ex-1 write function is_sorted(lst)
# def is_sorted(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] < lst[i + 1]:
#             return False
#     return True

# print(is_sorted([3, 2, 2])) #true
# print(is_sorted(['a', 'b'])) #false
# print(is_sorted([1, 4, 5])) #false

# #ex-2.1 change the value associated with the key 'y' to 25
# X = {'x': 10, 'y': 20, 'z': 30, 'a': 40}

# X['y'] = 30 #change the value associated with the key 'y' to 25, I accidently left it as 30 to test part 2.
# print(X)

# #ex-2.2 show how to remove the duplicate values from X
# #should have made a new change of the key 'y' to 30 here.
# Y = {}
# for key, value in X.items():
#     if value not in Y.values():
#         Y[key] = value

# print(Y)

# '''ex-3 Write a function called remove keys(mydict, keylist) that accepts two parameters: a dictionary called
# mydict and a list called keylist. remove keys(mydict, keylist) should remove all the keys contained in
# keylist from mydict and return the dictionary:'''
# def remove_keys(mydict, keylist):
#     for key in keylist: #iterate through the keylist 
#         if key in mydict:
#             del mydict[key]
#     return mydict

# d = { "key1" : "value1", "key2" : "value2", "key3" : "value3", "key4"
# : "value4" }
# keys = ["key1", "key3", "key5"]

# print(remove_keys(d, keys))

# '''Ex-4 Write a function called word frequencies(mylist) that accepts a strings of words and returns a dictionary
# where the keys are the words from the string of words and the values are the number of times that
# word appears in mylist:'''
# def word_frequencies(mylist):
#     freq_dict = {}
#     words = mylist.split()
#     for word in words:
#         word = word.strip(",.?!")  # Remove punctuation
#         if word in freq_dict:
#             freq_dict[word] += 1
#         else:
#             freq_dict[word] = 1
#     return freq_dict

# S = 'Fred fed Ted bread, and Ted fed Fred bread'
# # word_freq = {'Fred':2, 'fed':2, 'Ted':2, 'bread':2, 'and':1}

# print(word_frequencies(S))

# '''
# Exercise-5:
# Write a Python program to combine two dictionaries, adding values for common keys.
# '''
# def combine_dicts(d1, d2):
#     d3 = {}
#     for key in d1:
#         if key in d2:
#             d3[key] = d1[key] + d2[key]
#         else:
#             d3[key] = d1[key]
#     for key in d2:
#         if key not in d1:
#             d3[key] = d2[key]
#     return d3

# d1 = {'a': 100, 'd': 200, 'e':100}
# d2 = {'a': 200, 'c': 100, 'd':200}
# print(combine_dicts(d1, d2))

# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable 
# (which cannot be changed).
# However, the set itself is mutable. We can add or remove items from it.
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
setA.union(setB)
print(setA)
setA.intersection(setB)
print(setA)
setA.difference(setB)
print(setA)

# print(setA | setB) #union
# print(setA & setB) #intersection
# print(setA - setB) #difference

setA.add(6)
print(setA)
setA.update([7, 8, 9])
print(setA)
setA.add((1, 2, 8))
print(setA)
setA.update(['a', 'b'], ('a', 'c'))
print(setA)

setA.remove(1)
print(setA)
setA.discard(2)
print(setA)
