'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    if mCols == 0:
       li = ['row', 0, -2147483648]
    elif nRows == 0:
       li = ['columns', 0, -2147483648]
    else:
        sumRow = [0]*nRows
        sumCol = [0]*mCols
        for i in range(nRows):
            for j in range(mCols):
                sumRow[i] += arr[i][j]
                sumCol[j] += arr[i][j]
        li = ['row', 0, sumRow[0]]
        for i in range(nRows):
            if(sumRow[i] > li[2]):
                li[2] = sumRow[i]
                li[1] = i
        for j in range(mCols):
            if(sumCol[j] > li[2]):
                li[2] = sumCol[j]
                li[1] = j
                li[0] = 'column'
    print(li[0],li[1],li[2])
    #Your code goes here






#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
