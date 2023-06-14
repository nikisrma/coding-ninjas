"""
12345
 2345
  345
   45
    5
   45
  345
 2345
12345

"""
# 1.method

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(1,n+1):
    space = i-1
    for j in range(0,space):
        print(' ',end="")
    for j in range(i,n+1):
        print(j,end='')
    print()
for i in range(1,n):
    space = n-i-1
    for j in range(0,space):
        print(' ',end="")
    for j in range(n-i,n+1):
        print(j,end='')
    print()

    
#    2


from os import *
from sys import *
from collections import *
from math import *


num=int(input())
i=0
while num>i:
    spaces=1
    while spaces<=i:
        print(" ",end="")
        spaces=spaces+1
    j=1
    while num-i >=j:
        print(j+i,end="")
        j=j+1
    i=i+1
    print()
while i>1:
    spaces=1
    while spaces<=i-2:
        print(" ",end="")
        spaces=spaces+1
    j=num
    k=1
    while j>=i-1:
        print(i+k-2,end="")
        j=j-1
        k=k+1

    i=i-1
    print()
