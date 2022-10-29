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
