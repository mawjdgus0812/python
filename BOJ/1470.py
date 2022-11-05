import sys
from collections import deque
K = int(sys.stdin.readline())
check = 0
for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())
    m = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int,sys.stdin.readline().split())
        m[u].append(v)
        m[v].append(u)
    
    q = deque()
    color = True
    for i in range(1,V+1):
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            while q:
                l = q.popleft()
                for i in m[l]:
                    if visited[i] == 0:
                        q.append(i)
                        visited[i] = -1 * visited[l]
                    elif visited[i] == visited[l]:
                        color = False
                        
    print("YES" if color else "NO")