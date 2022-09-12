##### 내 풀이 ####

import sys
N = int(input())

for _ in range(N):
    li = list(sys.stdin.readline().rstrip())
    check = []
    check2 = 1
    for i in li:
        try:
            if i == '(':
                check.append(i)
            else:
                check.pop()
        except:
            check2 = 0
    if check2 and len(check)==0:
        print('YES')
    else:
        print('NO')

##### 1등 풀이 #####

from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')
