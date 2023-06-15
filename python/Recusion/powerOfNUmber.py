## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
## a, b = input().split()
## a = int(a)
## b = int(b)

def powerOfNumber(x, y):
    if y==1:
        return x
    else:
        return x*powerOfNumber(x, y-1)

a, b = input().split()
a = int(a)
b = int(b)
res = powerOfNumber(a, b)
print(res)
