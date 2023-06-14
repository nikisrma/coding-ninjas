from os import *
from sys import *
from collections import *
from math import *

def ninjaPuzzle(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<i:
                print(' ',end="")
            else:
                print('*',end='')
        print()
