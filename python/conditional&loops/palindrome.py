def checkPalindrome(num):
#Implement Your Code Here
	temp = num
	rev = 0
	while temp != 0:
		digit = temp % 10
		rev =  (rev*10 ) + digit
		temp = temp // 10
	if num == rev:
		return True
	else:
		return False

		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
