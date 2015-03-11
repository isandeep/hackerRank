
N = int(raw_input())

def palIndex(string):
    if string != string[::-1]:
        lst = list(string)
        counter = {ele:1 for ele in lst}
        print lst
        for ele in lst:
            newStr = string.replace(ele,'',counter[ele])
            counter[ele] += 1
            if len(newStr) == 1:
                return string.find(newStr)
            else:
                if newStr == newStr[::-1]:
                    print string
                    return string.find(ele)
    else:
        return -1

for i in range(N):
    print palIndex(raw_input())

def end_other(a,b):
    a, b = a.lower(), b.lower()
    if len(a) >= len(b):
        if a == b:
            return True
        else:
            return a[::-1][0:len(b)] == b[::-1]
    else:
        return b[::-1][0:len(a)] == a[::-1]

def cat_dog(a):
    return len(a.replace('cat',''))==len(a.replace('dog',''))

            
string = 'abcedabc'
def index1(string):
    a = len(string)
    lst = list(string)
    if string == string[::-1]:
        return -1
    else:
        for i in range(a):
            lst.pop(i)
            newStr = ''.join(lst)
            print newStr
            if newStr == newStr[::-1]:
                return i
            lst = list(string)
def index2(string):
    a = len(string)
    if string == string[::-1]:
        return -1
    else:
        for i in xrange(a/2):
            if string[i] != string[-i-1]:
                if string[i+1] == string[-i-1]:
                    return i
                else:
                    return (a - i)


string = raw_input()
assert 1 <= len(string) <= 1e3

letters = set('abcdefghijklmnopqrstuvwxyz')

string = set(string.lower())
if len(string) < 26:
    print 'not pangram'
if len(letters.intersection(string)) == 26:
    print 'pangram'
else:
    print 'not pangram'
