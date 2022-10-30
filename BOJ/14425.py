import sys


N, M = map(int,sys.stdin.readline().split())
S = []
sum = 0
for i in range(N+M):
    if i < N:
        S.append(str(sys.stdin.readline().rstrip()))
    else:
        a = str(sys.stdin.readline().rstrip()) 
        if a in S:
            sum += 1


print(sum)

###

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
S = set()
for _ in range(n):
    S.add(read().strip())

cnt = 0
for _ in range(m):
    word = read().strip()
    if word in S:
        cnt += 1

print(cnt)