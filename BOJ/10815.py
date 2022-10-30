import sys

N = int(sys.stdin.readline())
sangeun = list(map(int,sys.stdin.readline().split()))
sangeun_dict = {}
for i in sangeun:
    sangeun_dict[i] = 0
    
M = int(sys.stdin.readline())
haveornohave = list(map(int,sys.stdin.readline().split()))

for i in haveornohave:
    try:
        sangeun_dict[i]
        print(1, end=' ')
    except:
        print(0, end=' ')
        continue

##################

import sys

def test():
    input()
    b = set(input().split()) #내가 가진 값
    input()
    d = input().split()    #찾아야 하는 값
    res = ''
    for i in d:
        if i in b:
            res += '1 '
        else:
            res += '0 '
    print(res)

test()
