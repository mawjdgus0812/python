
import sys
from itertools import combinations

N = 9
shorts = []
for _ in range(N):
    shorts.append(int(sys.stdin.readline()))

for i in list(combinations(shorts, 7)):
    if sum(i) == 100:
        li = list(i)
        li.sort()
        for j in li:
            print(j)
