import sys

N, k = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))

l.sort(reverse=True)

print(l[k-1])

