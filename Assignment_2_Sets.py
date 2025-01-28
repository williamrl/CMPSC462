# Create a Python program that asks the user to enter two sets of comma-separated values. Use the
# string split() method to parse the line and then use the set() function to covert the lists to sets.
# Demonstrate set theory for the two sets by displaying the two sets and their relationship to each
# other as subset, superset, union, intersection, and difference.

def set_theory():
    set1 = input("Enter the first set of comma-separated values: ")
    set2 = input("Enter the second set of comma-separated values: ")

    set1 = set(set1.split(","))
    set2 = set(set2.split(","))

    print("Set 1: ", set1)
    print("Set 2: ", set2)

    if set1.issubset(set2):
        print("Set 1 is a subset of Set 2")
    else:
        print("Set 1 is not a subset of Set 2")

    if set1.issuperset(set2):
        print("Set 1 is a superset of Set 2")
    else:
        print("Set 1 is not a superset of Set 2")
        
    print("Union: ", set1.union(set2))
    print("Intersection: ", set1.intersection(set2))
    print("Difference: ", set1.difference(set2))

set_theory()

how can the last element of a set be deleted?
setA = {1, 2, 3, 4, 5}
setA.remove(5)
print(setA)
setA.discard(4)
print(setA)
#remove last element
setA.remove(3)
print(setA)

frozen set
A frozenset is a set that is immutable, meaning that once it is created, it cannot be changed.
frozenSetA = frozenset([1, 2, 3, 4, 5])
print(frozenSetA)

Write a Python program to check if two given sets have elements in common, remove those elements and return the set with unique elements?    5 points

def common_elements(set1, set2):
    common_elements = set1.intersection(set2)

    unique_set1 = set1.difference(common_elements)
    unique_set2 = set2.difference(common_elements)

    result = unique_set1.union(unique_set2)
    return result

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(common_elements(set1, set2))

