import sys

N = int(sys.stdin.readline())
s = 0
for i in range(1,N+1):
    s += (N//i)*i
print(s)