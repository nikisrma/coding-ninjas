"""
1
11
202
3003
"""
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    if i==1:
        print('1',end='')
    elif i==2:
        print('11',end='')
    else:
        j=1
        while j <= i:
            if j==1 or j==i:
                print(i-1,end='')
            else:
                print('0',end='')
            j = j+1
    print()
    i = i+1
