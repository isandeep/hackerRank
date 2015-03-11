# Solving the cheif hopper problem

# still not sure abt the solution
# import scipy.optimize as optimize
import math

# reading the input
N = int(raw_input())
hts = map(int, raw_input().split())

assert len(hts) == N

# constraints

if N < 1 or N > 10e4: raise ValueError
for h in hts:
    if h < 1 or h > 10e4: raise ValueError

Max = max(hts)
Min = min(hts)
htsNew = hts[0:hts.index(Max)+1]

def hopper(botE0):
    for h in htsNew:
        if botE0 < h:
            botE0 = -10000
            break
        else:
            botE0 = 2*botE0 - h
            print botE0
    return botE0

# Scipy not accepted
# sol = optimize.bisect(hopper, Min, Max, xtol = 1)

sol = Max
for i in xrange(Max+1):
    if hopper(i) >= 0:
        sol = min(sol, i)
print sol

# Bisection method
i = Max/2
if hopper(i) >= 0:
    i = i/2
else:
    i = (i+Max)/2

    
