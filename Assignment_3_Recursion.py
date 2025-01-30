# Write a recursive Python function that has a parameter representing a list of integers and returns
# the maximum stored in the list. Thinking recursively, the maximum is either the first value in the
# list or the maximum of the rest of the list, whichever is larger. If the list only has 1 integer, then
# its maximum is this single value, naturally
# L = [1, 2, 3, 4, 5]
# def maxList(L):
#     for i in L:
#         if len(L) == 1:
#             return L[0]
#         else:
#             return max(L[0], maxList(L[1:]))
        
# print(maxList(L))

# Run the Recursive Fibonacci function defined in the class notes with input a) 50 and b) 115

def Fibo(n):
    if n <= 1:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)
    
print(Fibo(50))
print(Fibo(115))