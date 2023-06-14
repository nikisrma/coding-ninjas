"""
  *
 ***
*****
 ***
  *
"""

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
mid = n//2+1
for i in range(1,mid+1):
    spaces = mid-i
    for j in range(spaces):
        print(' ',end='')
    for j in range((2*i)-1):
        print('*',end='')
    print()
for i in range(1,mid):
    for j in range(i):
        print(' ',end='')
    for j in range(1,n-(2*i)+1 ):
        print('*',end='')
    print()

