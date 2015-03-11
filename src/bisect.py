#########
# Code for Ahsish donation problem, HackerRank
# Using recursive bisection
###########

def sumOfSquares(n, i):
    return n-((i**3)/3 + (i**2)/2 + i/6) > 0


def bisect(N, lowerB=1.0, upperB=10e5):
    if not sumOfSquares(N, lowerB):
        return lowerB
    elif not sumOfSquares(N, upperB):
        upperB = (upperB + lowerB)/2
        return bisect(N, lowerB, upperB)
    else:
        while sumOfSquares(N, upperB):
            upperB += 1
        if sumOfSquares(N, int(upperB)):
            return int(upperB)
        else:
            return int(upperB-1)


T = int(raw_input())

for i in xrange(T):
    print bisect(int(raw_input()))


    
    
    
