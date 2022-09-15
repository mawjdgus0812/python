##### 내 풀이 #####
import sys
from collections import deque

N = int(input())
deq = deque()
for _ in range(N):
    com = sys.stdin.readline().split()
    # print(com)
    if 'push_front' in com: deq.appendleft(int(com[1]))
    elif 'push_back' in com: deq.append(int(com[1]))
    elif 'pop_front' in com: print(deq.popleft()) if len(deq) !=0 else print(-1)
    elif 'pop_back' in com: print(deq.pop()) if len(deq) !=0 else print(-1)
    elif 'size' in com: print(len(deq))
    elif 'empty' in com: print(1) if len(deq) ==0 else print(0)
    elif 'front' in com and not 'push' in com: print(deq[0]) if len(deq) !=0 else print(-1)
    elif 'back' in com and not 'push' in com: print(deq[-1]) if len(deq) !=0 else print(-1)
    
### 100 ms ###

##### 1등 풀이 #####
### 64ms ###

import sys
n_prob = int(sys.stdin.readline())
deque = []
for _ in range(n_prob):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        deque.insert(0, int(command.split()[1]))
    elif 'push_back' in command:
        deque.append(int(command.split()[1]))
    elif command == 'pop_front':
        print(deque.pop(0)) if deque else print(-1)
    elif command == 'pop_back':
        print(deque.pop()) if deque else print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        print(0) if deque else print(1)
    elif command == 'front':
        print(deque[0]) if deque else print(-1)
    elif command == 'back':
        print(deque[-1]) if deque else print(-1)
