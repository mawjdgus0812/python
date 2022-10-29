import sys
l = [int(sys.stdin.readline()) for _ in range(28)]
l.sort()

temo = [i for i in range(1,31)]

for j in temo:
    if j not in l:
        print(j)