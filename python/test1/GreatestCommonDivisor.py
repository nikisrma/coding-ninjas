

def findGcd(x, y):
    i = 1
    res =1
    while i <= x and i<=y:
        if x % i == 0 and y % i == 0:
            res= i
        i += 1
    return res
