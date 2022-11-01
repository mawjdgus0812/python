import sys

m = 0
n = 0
b = 0
for i in range(1,10):
    a = list(map(int,sys.stdin.readline().split()))
    if m < max(a):
        m = max(a)
        n = a.index(m)+1
        b = i

        
        
print(m)
print(b, n)
        
