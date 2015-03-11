#
###########Archery Challenge ##################
nC = int(raw_input()) # No.of Circles
rC = map(float, raw_input().split()) #radii
nL = int(raw_input()) # No.of line segments

cDict = {} # Co-ordinates
for i in range(1,nL+1):
    key = "pt" + str(i)
    cDict[key] = map(float, raw_input().split())

# Data checks
assert 1 <= nC <= 10e4
assert 1 <= nL <= 10e4
for i in rC:
    assert 0 < i < 10e5

for i in cDict.values():
    for j in i:
        assert abs(j) <= 10e5

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

## insert method

rC = qsort([r**2 for r in rC])
nQ = 0
for i in xrange(1,nL+1):
    lst = cDict["pt"+str(i)]
    print lst
    lst = qsort([lst[0]**2+lst[1]**2, lst[2]**2+lst[3]**2])
    print lst
    new = qsort(rC+lst)
    print new
    print nQ
    if lst[0] != lst[1]:
        nQ += new.index(lst[1])-new.index(lst[0])-1
    print nQ
    














