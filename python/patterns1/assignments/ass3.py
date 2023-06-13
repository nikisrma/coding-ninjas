"""
1
11
121
1221
"""


from os import *
from sys import *
from collections import *
from math import *


## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
i = 1

while i <= n:
    if i == 1:
        print('1', end="")
    elif i == 2:
        print('11', end="")
    elif i >= 2:
        j = 1
        while j <= i:
            if(j == 1 or j == i):
                print('1', end='')
            else:
                print('2', end="")
            j = j+1
    print('')
    i = i + 1

