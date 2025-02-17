# t(n) = 17 // O(1) // constant
# t(n) = 3log n // O(log n) // logarithmic
# t(n) = 20n - 4 // O(n) // linear
# t(n) = 2n^2 + 3n + 1 // O(n^2) // quadratic
# t(n) = 3n^3 + 2n^2 + 5n + 1 // O(n^3) // cubic
# t(n) = 2^n // O(2^n) // exponential
# t(n) = n! // O(n!) // factorial

# for(int c = n; c > n/2; c--) // O(n) // linear
# {
# print("hi");
# }
# multiplication of 2x2 by 2x2 matrix // O(n^3) // cubic

# O(1) is best
# O(2^n) is worst

# Give an analysis of the running time (Big-Oh notation) for each of the following 2 program fragments. Note that the
# running time corresponds here to the number of times the operation sum++ is executed. sqrt is the function that
# returns the square root of a given number.
import math

n = 100
j = 0
k = 0
# (a)
sum = 0
for i in range(int(math.sqrt(n)/2)):
    sum+=1

for j in range(int(math.sqrt(n)/2)):
    sum += 1

for k in range(8+j):
    sum += 1
# (a) has a time complexity of O(n) // linear
# why? because the for loop runs n times

print(sum)
# (b)
sum = 0
for i in range(int(math.sqrt(n)/2)):
    j = i
    for j in range(8+i):
        k = j
        for k in range(8+j):
            sum += 1
# (b) has a time complexity of O(n^3) // cubic
# why? because the for loop runs n^3 times
print(sum)

# (c) If it takes 10 ms to run program(b) for n=100, how long would you expect it to take to run the program for n=400?
# how long? 10ms * (400/100)^3 = 10ms * 64 = 640ms

# Design an algorithm that takes two arrays, and returns true if the arrays are disjoint, i.e. have no elements
# in common. Write down your algorithm as pseudocode. You don’t need to write a python code. Give the
# asymptotic analysis for time complexity in best-case and worst-case scenario.

def disjoint(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                return False
    return True

# best-case: O(1) // constant
# worst-case: O(n^2) // quadratic

print(disjoint([1, 2, 3], [4, 5, 6])) # True

# Consider the following list, List1 = [5, 30, 25, 60, 55, 15, 70, 35].
# What is the resulting list after two passes of the sorting phase i.e. after two iterations/recursive calls, if the
# following is performed? Show the steps using a rough sketch. You can draw the steps for each sorting algorithm
# in a paper, take a picture of it and attach it here.
# a) Selection Sort
# b) Insertion Sort
# c) Bubble Sort

a) Selection Sort 
[5, 30, 25, 60, 55, 15, 70, 35]
[5, 30, 25, 60, 55, 15, 70, 35]
[5, 15, 25, 60, 55, 30, 70, 35]
[5, 15, 25, 60, 55, 30, 70, 35]
[5, 15, 25, 30, 55, 60, 70, 35]
[5, 15, 25, 30, 35, 60, 70, 55]
[5, 15, 25, 30, 35, 55, 70, 60]
[5, 15, 25, 30, 35, 55, 60, 70]

b) Insertion Sort
[5, 30, 25, 60, 55, 15, 70, 35]
[5, 30, 25, 60, 55, 15, 70, 35]
[5, 25, 30, 60, 55, 15, 70, 35]
[5, 25, 30, 60, 55, 15, 70, 35]
[5, 25, 30, 55, 60, 15, 70, 35]
[5, 15, 25, 30, 55, 60, 70, 35]
[5, 15, 25, 30, 55, 60, 70, 35]
[5, 15, 25, 30, 35, 55, 60, 70]

c) Bubble Sort
[5, 30, 25, 60, 55, 15, 70, 35]
[5, 25, 30, 60, 55, 15, 70, 35]
[5, 25, 30, 55, 60, 15, 70, 35]
[5, 25, 30, 55, 60, 15, 70, 35]
[5, 25, 30, 55, 15, 60, 70, 35]
[5, 25, 30, 55, 15, 60, 70, 35]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]
[5, 25, 30, 55, 15, 60, 35, 70]


# Assume that an Insertion sort algorithm in the worst case takes 4 minutes and 10 seconds for an input of pool size
# 30. What will be the maximum input pool size of a problem that can be solved in 20 minutes and 50 seconds in the
# worst case?

# 4 minutes and 10 seconds = 250 seconds
# 20 minutes and 50 seconds = 1250 seconds
# 30 * 250 = 7500 seconds
# 7500 / 1250 = 6
# 30 * 6 = 180
# 180 is the maximum input pool size of a problem that can be solved in 20 minutes and 50 seconds in the
# worst case
