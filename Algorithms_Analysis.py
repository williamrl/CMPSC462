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