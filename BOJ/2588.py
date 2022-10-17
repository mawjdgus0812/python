import sys

A = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().rstrip()))

a = int(A*B[-1])
b = int(A*B[-2])
c = int(A*B[-3])
print(a)
print(b)
print(c)

print(a+b*10+c*100)