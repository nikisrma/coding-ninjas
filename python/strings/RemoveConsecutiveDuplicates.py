
from sys import stdin
def removeConsecutiveDuplicates(string):
    str1 = ''
    for i in range(len(string)):
        if i < len(string)-1:
            if string[i] != string[i+1]:
                str1 += string[i]
        else:
            str1 += string[i]
    print(str1)


string = stdin.readline().strip()

removeConsecutiveDuplicates(string)







