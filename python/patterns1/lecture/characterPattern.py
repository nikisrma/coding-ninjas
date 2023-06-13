"""
A
BC
CDE
DEFG
"""

## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while(i<=n):
    j=1
    while j<=i:
        print(chr(64+i+j-1),end="")
        j = j+1
    print()
    i = i+1
