"""
       1
     232
   34543
 4567654
567898765
"""
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i=1
while i<=n:
    spaces = n-i
    j=1
    while j<=spaces:
        print(' ',end='')
        j=j+1
    k=i
    while k<=(2*i)-1:
        print(k,end='')
        k= k+1
    m=1
    while m<i:
        print((2*i)-m-1,end='')
        m=m+1
    print()
    i = i+1


