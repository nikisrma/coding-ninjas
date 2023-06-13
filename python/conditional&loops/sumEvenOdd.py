n  = input()
arr = [int(d) for d in str(n)]
evenSum = 0
oddSum = 0
for i in arr:
    if(i%2==0):
        evenSum += i
    else:
        oddSum += i
print(evenSum," ",oddSum)
