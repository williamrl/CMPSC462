# # x = [1, 'a', 5] #list of integers and strings
# # y = [2, 3] #list of integers
# # #print(x+y) #concatenates the two lists

# # #print(x*2) #prints the list x twice
# # #print(x/1) #prints the list x once

# # L2 = [1, 2, 3, 4, 5*5, 'a', 6] #list of integers and strings
# # for i in range(0, 5):
# #     print(L2[i])

# # print(L2[0:5]) #prints the elements from index 0 to 4

# # L2.append(10) #adds 10 to the end of the list
# # print(L2)

# # L2.append(x) #adds the list x to the list L2
# # print(L2)

# # L2.extend(x) #adds the elements of x to the list L2
# # print(L2)

# # L2.pop(5) #removes the element at index 5
# # print(L2)

# # del L2[0] #deletes the element at index 0
# # print(L2)

# # a = L2.pop(5) #removes the element at index 5
# # print(L2)
# # print(a)

# # x = [1, 2, 3]
# # print(x)
# # b = x.pop() #removes the last element from the list
# # print(b)
# # y = x[1:3] #slicing
# # print(y)
# # del x[1] #deletes the element at index 1
# # print(x)
# # x.remove(1) #removes the element 1 from the list
# # print(x)


# # char = ['a', 'c', 'b', 'e', 'd', 'g', 'i', 'h']
# # char.sort() #sorts the list in ascending order by turning the characters into their ASCII values and then sorting them
# # print(char)

# # num = [1, 3, 2, 5, 4, 7, 6, 9, 8]
# # num.sort() #sorts the list in ascending order by turning the numbers into their ASCII values and then sorting them
# # print(num)

# # nums = [3, 41,12, 9, 74, 15]
# # print(len(nums)) #prints the length of the list
# # print(max(nums)) #prints the maximum value in the list
# # print(min(nums)) #prints the minimum value in the list
# # print(sum(nums)) #prints the sum of the list
# # print(sum(nums)/len(nums)) #prints the average of the list

# # myList = [2, 4, 9] #list of integers
# # yourList = [item ** 2 for item in myList] #squares each element in myList and stores it in yourList
# # print(yourList) #prints the square of each element in myList

# # myList = [2, 5, 9] #list of integers
# # yourList = [item ** 2 for item in myList if (item%2) == 0] #squares each element in myList if the element is even and stores it in yourList
# # print(yourList) #prints the square of each even element in myList

# # nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #list of lists
# # complexNestedList = [1, [2, 3], [4, [5, 6, [7], 8], 9]]
# # print(complexNestedList[2][1][1])   #prints 6
# # print(nestedList[2][1][3])

# # wds = ["red", "blue", "green"] #list of strings
# # glue = ';' #string
# # s = glue.join(wds) #joins the elements of the list with the string glue
# # print(s) #prints red;blue;green
# # print(wds) #prints ['red', 'blue', 'green']

# # print("***".join(wds)) #prints red***blue***green
# # print("".join(wds)) #prints redbluegreen

# # b = glue.split(s) #splits the string s using the string glue
# # print(b) #prints ['red', 'blue', 'green']

# # dict = {'apple': 1, 'banana': 2, 'oranges': 3, 'pears': 4} #dictionary // 'apple' is the key and 1 is the value
# # print(dict)
# # print(dict['apple']) #prints 1
# # dict['apple'] = 5 #changes the value of the key 'apple' to 5
# # print(dict)
# # dict['grapes'] = 6 #adds a new key-value pair to the dictionary
# # print(dict)

# # for key in dict:
# #     print(key, dict[key]) #prints the key-value pairs in the dictionary

# d = {'user':'vinay', 'pswd':'123', 'id':14} #dictionary
# print(d.keys()) #prints the keys in the dictionary
# print(d.values()) #prints the values in the dictionary
# print(d.items()) #prints the key-value pairs in the dictionary (in tuples)

# #aliasing
# a = [1, 2, 3] #list
# b = a #aliasing
# print(a is b) #prints True
# b[0] = 5 #changes the first element of the list b
# print(a) #prints [5, 2, 3]
# print(b) #prints [5, 2, 3]

# #copying
# a = [1, 2, 3] #list
# b = a[:] #copying
# print(a is b) #prints False
# b[0] = 5 #changes the first element of the list b
# print(a) #prints [1, 2, 3]
# print(b) #prints [5, 2, 3]


# opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'} #dictionary
# alias = opposites #aliasing

# print(alias is opposites) #prints True

# alias['right'] = 'left' #changes the value of the key 'right' in the dictionary alias
# print(opposites['right']) #prints left

# acopy = opposites.copy() #copying
# acopy['right'] = 'left' #does not change opposites


# numberGames = {} #empty dictionary
# numberGames[(1, 2, 4)] = 8 #adds a key-value pair to the dictionary
# numberGames[(4, 2, 1)] = 10 #adds a key-value pair to the dictionary
# numberGames[(1, 2)] = 12 #adds a key-value pair to the dictionary
# print(numberGames) #prints {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# sum = 0
# for k in numberGames:
#     sum += numberGames[k] #adds the values of the dictionary

# print(len(numberGames) + sum) #prints 33

# boxes = {} #empty dictionaries
# jars = {} #empty dictionaries
# crates = {} #empty dictionaries
# boxes['cereal'] = 1 #adds the key-value pair 'cereal': 1 to the dictionary boxes
# boxes['candy'] = 2 #adds the key-value pair 'candy': 2 to the dictionary boxes
# jars['honey'] = 4  #adds the key-value pair 'honey': 4 to the dictionary jars
# crates['boxes'] = boxes #adds the dictionary boxes to the dictionary crates
# crates['jars'] = jars #adds the dictionary jars to the dictionary crates
# print(len(crates['boxes'])) #prints 2

