
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    if(len(string1)!=len(string2)):
        return False
    else:
        string1 = sorted(string1)
        string2 = sorted(string2)
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
        else: return True



#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

