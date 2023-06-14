from os import *
from sys import *
from collections import *
from math import *


n = int(input())

len1 = len(str(n))

sum = 0
temp = n
while n > 0:
    digit = n % 10
    sum +=  (digit ** len1)
    n =n // 10

if sum== temp:
    print("true")
else:
    print("false")
