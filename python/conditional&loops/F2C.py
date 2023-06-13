# Read input as sepcified in the question
# Print output as specified in the question

s = int(input())
e = int(input())
w = int(input())

while s <= e:
    c = ((s-32)*5)/9
    print(s , int(c))
    s = s+w
