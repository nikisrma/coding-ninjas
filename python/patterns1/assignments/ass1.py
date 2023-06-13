"""
1
11
111
1111
"""

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
    j= 1
    while j<=i:
        print(1,end='')
        j = j+1
    print()
    i = i+1
