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
