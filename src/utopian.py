# Build an utopian tree
no_trees = int(raw_input())
if no_trees > 10 : raise NameError("See constraints")

years = []
for x in xrange(no_trees):
    years.append(int(raw_input()))

##print years

# data checks
for val in years:
    if val > 60 and val < 0 : raise NameError("integer overflow")

# Build the tree

def build_tree(yr1, int_ht = 1):
    for x in xrange(1, yr1+1):
        if x % 2 == 1 :
            int_ht = int_ht * 2
        else:
            int_ht = int_ht + 1
    return(int_ht)

##int_ht = 1 # Intialize the height

years = [build_tree(x) for x in years]

for t,val in enumerate(years):
    print val
##    print "Height of %dst utopian tree is %d"%(t+1,val)

    
    




    

