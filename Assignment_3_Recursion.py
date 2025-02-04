# Write a recursive Python function that has a parameter representing a list of integers and returns
# the maximum stored in the list. Thinking recursively, the maximum is either the first value in the
# list or the maximum of the rest of the list, whichever is larger. If the list only has 1 integer, then
# its maximum is this single value, naturally

# L = [5]
# L2 = [1, 14, 3, 12, 5]
# def maxList(L):
#     for i in L:
#         if len(L) == 1:
#             return L[0]
#         else:
#             return max(L[0], maxList(L[1:]))
        
# print(maxList(L))
# print(maxList(L2))

# Run the Recursive Fibonacci function defined in the class notes with input a) 10 and b) 15.
def fibonacciSmall(n):
    if n == 0: # base case
        return 0 
    elif n == 1: 
        return 1 
    else:
        return fibonacciSmall(n-1) + fibonacciSmall(n-2) # recursive case 

print('This is fibo for the number 10: ', fibonacciSmall(10))
print('This is fibo for the number 15: ', fibonacciSmall(15))

# # Run the Recursive Fibonacci function defined in the class notes with input a) 50 and b) 115.
# # memoization is used to store the values of the fibonacci sequence
def fibonacciLarge(n, memo={}): 
    if n in memo: # if n is already in the memo dictionary, return the value of
        return memo[n] # the key n
    if n == 0: # base case
        return 0
    elif n == 1: 
        return 1
    else: # recursive case using memoization to store larger values of n (much faster method for larger numbers)
        memo[n] = fibonacciLarge(n-1, memo) + fibonacciLarge(n-2, memo)
        return memo[n]

print('This is fibo for the number 50: ', fibonacciLarge(50))
print('This is fibo for the number 115: ', fibonacciLarge(115))

# # Write a recursive function to calculate the sum of the positive integers of n+(n-2)+(n-4)...

# def sumOfPositiveIntegers(n):
#     if n <= 0: # base case
#         return 0
#     else: # recursive case 
#         return n + sumOfPositiveIntegers(n-2)

# print('This is the sum of positive integers for 113: ', sumOfPositiveIntegers(113))

# Write a recursive function to calculate the value of 'a' to the power 'b'?
def power(a, b):
    if b == 0: # base case
        return 1
    else: # recursive case 
        return a * power(a, b-1)
    
print('This is the power of 2 to the power of 3: ', power(2, 3))