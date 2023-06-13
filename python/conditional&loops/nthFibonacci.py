from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = 0
b = 1
sum = 0
count = 1
while(count <= n):
  count += 1
  a = b
  b = sum
  sum = a + b
print(sum)

