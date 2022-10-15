import sys

N, M = map(int, sys.stdin.readline().split())
lis = []
look = []
for _ in range(N):
    lis.append(sys.stdin.readline().rstrip())

for _ in range(M):
    look.append(sys.stdin.readline().rstrip())
    
duplicate = list(set(lis) & set(look))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)