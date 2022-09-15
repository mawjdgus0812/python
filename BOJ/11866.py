##### 내 풀이 #####

import sys

# 1, 2, 3, 4, 5, 6, 7
#       -
#                -
#    -        
#                   -

N,K = map(int,sys.stdin.readline().split())

li = list(range(1,N+1))
key = 0
temp = K-1
order = []
while li:
    key = (key+temp)%len(li)
    order.append(li.pop(key))

print('<'+', '.join(map(str,order))+'>')

##### 1등 풀이 #####

N, K = map(int, input().split())
l = list(range(1, N+1))
p = list()
i = 0
while l:
    i = (i+K-1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')
