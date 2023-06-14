
from sys import stdin


def highestOccuringChar(string) :
	#Your code goes here
	li = [0]*256
	max = -1
	ch =''
	for e in string:
		li[ord(e)] += 1
	for e in string:
		if max < li[ord(e)]:
			max =  li[ord(e)]
			ch = e
	return ch






#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
