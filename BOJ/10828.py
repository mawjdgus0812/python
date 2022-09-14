##### 내 풀이 #####
import sys

N = int(input())
stack = []
for _ in range(N):
    com = sys.stdin.readline().split()
    if 'push' in com:
        stack.append(int(com[1]))
    elif 'pop' in com:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in com:
        print(len(stack))
    elif 'empty' in com:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif 'top' in com:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

##### 1 등 풀이 #####
import sys
stack = []
orders = sys.stdin.read().splitlines()
for order in orders:
    if 'push' in order:
        stack.append(order.split()[1])
    elif 'pop' in order:
        print(stack.pop()) if stack else print(-1)
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        print(0) if stack else print(1)
    elif 'top' in order:
        print(stack[-1]) if stack else print(-1)