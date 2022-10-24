import sys

N = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))

v = int(sys.stdin.readline())

cnt = 0

for i in l:
    if i == v:
        cnt += 1
        
        
print(cnt)