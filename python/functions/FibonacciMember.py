import math
def perfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def checkMember(n):
#Implement Your Code Here
    return perfectSquare(5*n*n+4) or perfectSquare(5*n*n-4)

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
