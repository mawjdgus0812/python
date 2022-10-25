import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

b = list(set(a))
b.sort()

dic = {}
for i, num in enumerate(b):
    dic[num] = i
for i in a:
    print(dic[i],end=' ')