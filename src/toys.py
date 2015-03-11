# code for toys problem hackerRank

# Problem: given toys with weights, miminize the no. of items to buy to
# get the whole set. offer: buy toy(w) get toys with wts b/w w and w+4

# Approach: Sort the input and sequentially remove until there are
# none left

# read input
N = int(raw_input())
wts = raw_input().split()

#convert wts to integers
wts = [int(w) for w in wts]

#check for constraints
if N < 1 or N > 10e4: raise ValueError
for w in wts:
    if w < 0 or w > 10e3: raise ValueError

assert len(wts) == N

# Keep only unique weights
wts = set(wts)

#buy the minimum weight
items_bgt = []

while len(wts) > 0:
    item = min(wts)
    items_bgt.append(item)
    wts = wts - set(range(item, item+5))
print len(items_bgt)

