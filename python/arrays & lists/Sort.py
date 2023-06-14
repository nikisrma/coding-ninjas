from sys import stdin

def sortZeroesAndOne(arr, n) :
    countOne = arr.count(1)
    countZero = arr.count(0)
    for i in range(n):
        if i < countZero:
            arr[i] = 0
        else:
            arr[i] = 1
    #Your code goes here

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    # print()

    t -= 1