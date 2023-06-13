 """
    *
   *** 
  *****
 *******
"""
## without using multiple loops


from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n= int(input())
i=1
while i<=n:
    j=1
    while j<=n+i-1:
        if j <= n-i:
            print(' ',end="")
        else:
            print('*',end='')
        j=j+1
    print()
    i=i+1
    
    
    
#Using loops
from os import *
from sys import *
from collections import *
from math import *


num=int(input())
i=1

while i<=num:
    j = 0
    while j<num-i:
        print(" ",end="")
        j=j+1
    k=0
    while k<i:
        print("*",end="")
        k=k+1
    k=1
    while k<i:
        print("*",end="")
        k=k+1
    i=i+1
    print()
