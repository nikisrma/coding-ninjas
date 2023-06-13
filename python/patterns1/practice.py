"""
12344321
123**321
12****21
1******1
"""
n = int(input())
i = 1
while i<=n:
    j = 1
    while j <= 2*n:
        if j<=n-i+1:
            print(j,end='')
        elif j>n-i+1 and j<n+i:
            print('*',end='')
        else:
            print((2*n)-j+1,end='')
        j = j+1
    print()
    i= i+1
    


"""
4555
3455
2345
1234
"""


n = int(input())
i = 1
while i<=n:
    j=1
    while j<=n:
        if j>i:
            print('5',end='')
        else:
            print(n-i+j,end='')
        j = j+1
    print()
    i=i+1
