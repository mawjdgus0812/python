##### 내 풀이 #####
import sys
from collections import deque

queue = deque()

N = int(input())

for _ in range(N):
    com = sys.stdin.readline()
    if 'push' in com:
        queue.append(int(com.split()[1]))
    elif 'pop' in com:
        print(-1) if len(queue) == 0 else print(queue.popleft())
    elif 'size' in com:
        print(len(queue))
    elif 'empty' in com:
        print(1) if len(queue) == 0 else print(0)
    elif 'front' in com:
        print(-1) if len(queue) == 0 else print(queue[0])
    elif 'back' in com:
        print(-1) if len(queue) == 0 else print(queue[-1])
        
##### 1등 풀이 #####

from sys import stdin

read = stdin.readline

N = int(read())
queue = []
answer = []
command = {
    "push": queue.append,
    "pop": lambda q: q.pop(0) if q else '-1',
    "size": lambda q: str(len(q)),
    "empty": lambda q: '0' if q else '1',
    "front": lambda q: q[0] if q else '-1',
    "back": lambda q: q[-1] if q else '-1'
}

for _ in range(N):
    o = read().rstrip()
    if len(o) > 5:
        o = o.split()
        command[o[0]](o[1])
    else:
        answer.append(command[o](queue))

print('\n'.join(answer))