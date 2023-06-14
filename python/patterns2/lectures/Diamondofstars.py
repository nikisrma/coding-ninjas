"""
  *
 ***
*****
 ***
  *
"""
from os import *
from sys import *
from collections import *
from math import *

n = int(input())
m = n//2 + 1
for i in range(1, m+1, 1):
    for sp in range(m-i):
        print(' ', end='')

    for j in range(2*i - 1):
        print('*', end='')

    print()

for i in range(1, m, 1):
    for sp in range(i):
        print(' ', end='')

    for j in range(1, n-2*i + 1, 1):
        print('*', end='')
    print()

