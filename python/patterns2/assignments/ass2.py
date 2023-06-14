"""
*000*000*
0*00*00*0
00*0*0*00
000***000

"""
from os import *
from sys import *
from collections import *
from math import *

n = int(input())
i=1
rows = (2*n)+1
while i<=n:
    j=1
    while j<=rows:
        if j==i or j==(rows//2)+1 or j==rows+1-i:
            print('*',end='')
            j=j+1
        else:
            print('0',end='')
            j=j+1
    print()
    i=i+1
