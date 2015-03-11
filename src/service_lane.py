## Helping calvin to choose medium of transport

# read input
N,T = raw_input().split()
lane_width = list(raw_input().split())

# convert input into integers
N, T = int(N), int(T)
lane_width = [int(x) for x in lane_width]


# Take input from test cases
test_cases = []
for x in xrange(T):
    test_cases.append(raw_input("test case here:").split())
for i, t in enumerate(test_cases):
    t = [int(x) for x in t]
    test_cases[i] = t


# Perform data checks
if N < 2 or N > 100000: raise NameError("Please check constraints")
if T < 1 or T > 1000: raise NameError("Please check constraints")
for t, val in enumerate(test_cases):
    i, j = val[0], val[1]
    a = j-i+1
    if i < 0 or j >= N : raise NameError("Please check test case %d", t+1)
    if i >= j: raise NameError("Please check test case %d", t+1)
    if a < 2 or a > min([N, 1000]): raise NameError("See constraint 4")
for w in lane_width:
    if w < 1 or w > 3 : raise NameError("Width is not in specified range")
if len(lane_width) > N : raise NameError("See constraints")


# print output
print lane_width
print test_cases
print lane_width[1:4]
for t, val in enumerate(test_cases):
    i, j = val[0],val[1]
    print lane_width[i:j+1],min(lane_width[i:j+1])
    
