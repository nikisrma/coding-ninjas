"""
 A
 BB
 CCC
"""
from os import *
from sys import *
from collections import *
from math import *


## Read input as specified in the question.
## Print output as specified in the question.


N = int(input())
row = 1
while row <= N:
    col = 1
    while col <= row:
        print(chr(64+row), end="")
        col = col+1
    row = row+1
    print()
