import itertools
import math

# reading the input
N = int(raw_input())

seqDict, seqLen = {}, []

for i in xrange(1, N+1):
    key = "seq" + str(i)
    seqLen.append(int(raw_input()))
    seqDict[key] = map(int, raw_input().split())

assert len(seqDict.keys()) == N

#constraints

if not 1 <= N <= 10e2: raise ValueError
for k in seqLen:
    if not 2 <= k <= 10e2: raise ValueError
for seq in seqDict.values():
    assert len(seq) == len(set(seq))
    for k in seq:
        if not 1 <= k <= 10e5: raise ValueError

# #function to get unique elem by preserving order
# def set_order(seq):
#     # Order preserving
#     seen = set()
#     return [x for x in seq if x not in seen and not seen.add(x)]
# seqOut = []
# for seq in itertools.izip_longest(*seqDict.values()):
#     # print seq
#     seqOut.extend(set(seq))
#     print seqOut

# seqOut = set_order(seqOut[::-1])
# res = seqOut[::-1]
# res = [x for x in res if x is not None]
# for item in res:
#     print item,

# Approach 2

# sort the input dict of sequences
from collections import OrderedDict

dictSorted = OrderedDict(sorted(seqDict.items(),
             key = lambda x: len(x[1]), reverse = True))

items = dictSorted.values()[:]
print items

for i, item in enumerate(items):
    cuts = []
    if i == 0:
        buildList = item
    else:
        print "moved to index", i
        intersect = [x for x in buildList if x in item]
        if intersect:
            print intersect
            indices = [buildList.index(x) for x in intersect]
            indices = set(indices)
            print indices
            for j in indices:
                cuts.append(item[0:j])
                item = item[j+1:]
            # print cuts
            for lst in cuts:
                for a in lst:
                    for b in buildList:
                        if a < b:
                            idx = buildList.index(b)
                            buildList.insert(idx, a)
                            break
            print buildList
                # temp = buildList
                # if a is not None and not a:
                #     temp = list(set(temp.append(a)))
                #     idx = temp.index(a)
                #     for k, val in enumerate(lst):
                #         buildList.insert(k+idx, val)
                #         print buildList
        else:
            print "executing else intersect at index",i
            for a in item:
                for b in buildList:
                    if a < b:
                        idx = buildList.index(b)
                        buildList.insert(idx, a)
                        break
            print buildList
