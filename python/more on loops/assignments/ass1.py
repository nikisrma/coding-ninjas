# 1. Binary pattern
"""
1111
000
11
0
"""


from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n= int(input())
for i in range(1,n+2):
    for j in range(1,n+2-i):
        if i%2 == 1:
            print('1',end="")
        else:
            print('0',end="")
    print()
    
    
#2 
