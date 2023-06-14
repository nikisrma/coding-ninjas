
def printTable(start,end,step):
	while start <= end:
		f = ((start-32)*5)/9
		print(start,end = '\t')
		print(int(f))
		start = start+step
#Implement Your Code Here
	pass 

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





