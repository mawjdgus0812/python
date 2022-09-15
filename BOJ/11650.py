##### 내 풀이 #####

import sys

N = int(input())
x_y_li = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    x_y_li.append((x,y))

x_y_li.sort(key=lambda x : (x[0],x[1]))
for a in x_y_li:
    print(a[0],a[1])
    
    
    
##### 1등 풀이 #####

import sys

li = sys.stdin.readlines()[1:]
li.sort(key=lambda x: int(x.split()[1]))
li.sort(key=lambda x: int(x.split()[0]))
sys.stdout.write("".join(li))