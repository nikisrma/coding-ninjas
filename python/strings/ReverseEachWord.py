
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	li = string.split(' ')
	for i in range(len(li)):
		li[i] = li[i][::-1]
	stri = (' ').join(li)
	return stri


#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
