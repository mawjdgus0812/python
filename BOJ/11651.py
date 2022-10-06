

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int,input().split())
    lst.append((x,y))

lst.sort(key=lambda x : (x[1],x[0]))

for a in lst:
    print(a[0],a[1])

############

import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()

lst = sys.stdin.readlines()[1:]

lst.sort(key=lambda x: int(x.split()[0]))
lst.sort(key=lambda x: int(x.split()[1]))
print(''.join(lst))