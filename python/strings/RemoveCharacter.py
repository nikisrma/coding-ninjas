
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	res = ''
	for e in string:
		if e!=ch:
			res += e
	return res




#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
