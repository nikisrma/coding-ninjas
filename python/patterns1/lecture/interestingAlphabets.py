"""
E
DE
CDE
BCDE
ABCDE
"""
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        print(chr(64+n+j-i),end="")
        j = j+1
    print()
    i = i+1
