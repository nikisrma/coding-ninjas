"""
   1
  12
 123
1234

"""
## Read input as specified in the question
## Print the required output in given format

n = int(input())
i = 1
while i<=n:
    j=1
    spaces=1
    while spaces<n-i+1:
        print(' ',end='')
        spaces = spaces +1
    while j<=i:
        print(j,end="")
        j= j+1
    print()
    i=i+1
