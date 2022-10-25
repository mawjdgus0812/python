import sys

a = [int(sys.stdin.readline()) for _ in range(5)]
print(int(sum(a)/5))
a.sort()
print(a[2])