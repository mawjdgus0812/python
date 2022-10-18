import sys

a = list(map(int,sys.stdin.readline().rstrip()))
a.sort(reverse=True)

for i in a:
    print(i, end='')
    
###

print(''.join(sorted(input())[::-1]))