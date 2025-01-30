# def j():
#     j() # Recursive call

L = [1, 2, 3, 4, 5]

def listSum(L):
    sum = 0
    
    for i in L:
        sum += i
    return sum

print(listSum(L))

#recursion is 1+2+3+4+5 = 15
#             1+(2+3+4+5)
#               2+(3+4+5)
#                 3+(4+5)
#                   4+5
def listSumR(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + listSumR(L[1:])
    
print(listSumR(L))

# Write a recursive function to perform Factorial
def Factorial(x):
    if x == 1:
        return 1
    else:
        return x * Factorial(x-1)
    
print(Factorial(5))

def Fibo(n):
    if n <= 1:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)

print(Fibo(10))

#reverse a list through recursion
def reverse(L):
    if len(L) == 0:
        return []
    else:
        return reverse(L[1:]) + [L[0]]

print(reverse([1, 2, 3, 4, 5]))

#multiple of 3 through recursion
def multiple3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return multiple3(n-1) + 3
    
print(multiple3(21))

#sum of natural numbers through recursion
def sumNatural(n):
    if n == 0:
        return 0
    else:
        return sumNatural(n-1) + n
    
print(sumNatural(5))

# Write a Python program to calculate the sum of the positive even integers of n+(n-2)+(n-4)...
def sumEven(n):
    if n == 0:
        return 0
    else:
        return sumEven(n-2) + n

print(sumEven(10))

# Write a Python program to calculate the value of 'a' to the power 'b'.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)