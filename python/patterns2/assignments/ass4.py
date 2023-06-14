"""
* 
 * * 
  * * * 
   * * * * 
  * * * 
 * * 
* 
"""
## Read input as specified in the question.
## Print output as specified in the question.
n= int(input())
i = 1
while i<=n:
    if i<=(n//2)+1:
        j=1
        while j<i:
            print(' ',end='')
            j= j+1
        k=0
        while k<i:
            print('* ',end='')
            k=k+1
    else:
        j=1
        while j<n-i+1:
            print(' ',end='')
            j= j+1
        k=0
        while k<n-i+1:
            print('* ',end='')
            k=k+1
    print()
    i +=1


"""
"""
