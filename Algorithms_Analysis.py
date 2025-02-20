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

#selection sort // O(n^2) // quadratic // it is best for small data sets
# 4, 2, 1, 3 // it sorts by finding the smallest number and swapping it with the first number
# 1, 2, 4, 3 // 1 is the smallest number so it swaps with 4 
# 1, 2, 3, 4 // 3 is the smallest number not in order so it swaps with 4
# selection_sort = [64, 25, 12, 22, 11]
# for i in range(len(selection_sort)):
#     min_idx = i
#     for j in range(i+1, len(selection_sort)):
#         if selection_sort[min_idx] > selection_sort[j]:
#             min_idx = j
#     selection_sort[i], selection_sort[min_idx] = selection_sort[min_idx], selection_sort[i]
# print(selection_sort)

# insertion sort // O(n^2) // quadratic // it is best for small data sets
# 4, 2, 1, 3 // it sorts by comparing the first number with the second number and swapping if the first number is greater
# 2, 4, 1, 3 // 2 is less than 4 so it swaps
# 1, 2, 4, 3 // 1 is less than 4 so it swaps
# 1, 2, 3, 4 // 3 is less than 4 so it swaps
# insertion_sort = [64, 25, 12, 22, 11]
# for i in range(1, len(insertion_sort)):
#     key = insertion_sort[i]
#     j = i-1
#     while j >= 0 and key < insertion_sort[j]:
#         insertion_sort[j+1] = insertion_sort[j]
#         j -= 1
#     insertion_sort[j+1] = key
# print(insertion_sort)

# bubble sort // O(n^2) // quadratic // it is best for small data sets //best case: O(n) // linear //
# 4, 2, 1, 3 // it sorts by comparing the first number with the second number and swapping if the first number is greater
# 2, 4, 1, 3 // 2 is less than 4 so it swaps
# 2, 1, 4, 3 // 2 is greater than 1 so it swaps
# 2, 1, 3, 4 // 4 is greater than 3 so it swaps
# 1, 2, 3, 4 // 2 is greater than 1 so it swaps
# bubble_sort = [64, 25, 12, 22, 11]
# for i in range(len(bubble_sort)):
#     for j in range(len(bubble_sort)-1):
#         if bubble_sort[j] > bubble_sort[j+1]:
#             bubble_sort[j], bubble_sort[j+1] = bubble_sort[j+1], bubble_sort[j]
# print(bubble_sort)


# merge sort // O(n log n) // logarithmic // it is best for large data sets
# 64, 25, 12, 22, 11 // it sorts by dividing the list into two halves and then sorting each half and then merging them
# 64, 25, 12 // 64, 25 // 64 // 25 // 25, 64 // 12 // 22 // 11 // 12, 22 // 11 // 11, 12, 22 // 11, 12, 22, 25, 64
# merge_sort = [64, 25, 12, 22, 11]
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L)
#         merge_sort(R)
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr
# print(merge_sort(merge_sort))


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

# a) Selection Sort 
# [5, 30, 25, 60, 55, 15, 70, 35]
# [5, 30, 25, 60, 55, 15, 70, 35]
# [5, 15, 25, 60, 55, 30, 70, 35]
# [5, 15, 25, 60, 55, 30, 70, 35]
# [5, 15, 25, 30, 55, 60, 70, 35]
# [5, 15, 25, 30, 35, 60, 70, 55]
# [5, 15, 25, 30, 35, 55, 70, 60]
# [5, 15, 25, 30, 35, 55, 60, 70]

# b) Insertion Sort
# [5, 30, 25, 60, 55, 15, 70, 35]
# [5, 30, 25, 60, 55, 15, 70, 35]
# [5, 25, 30, 60, 55, 15, 70, 35]
# [5, 25, 30, 60, 55, 15, 70, 35]
# [5, 25, 30, 55, 60, 15, 70, 35]
# [5, 15, 25, 30, 55, 60, 70, 35]
# [5, 15, 25, 30, 55, 60, 70, 35]
# [5, 15, 25, 30, 35, 55, 60, 70]

# c) Bubble Sort
# [5, 30, 25, 60, 55, 15, 70, 35]
# [5, 25, 30, 60, 55, 15, 70, 35]
# [5, 25, 30, 55, 60, 15, 70, 35]
# [5, 25, 30, 55, 60, 15, 70, 35]
# [5, 25, 30, 55, 15, 60, 70, 35]
# [5, 25, 30, 55, 15, 60, 70, 35]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]
# [5, 25, 30, 55, 15, 60, 35, 70]


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
