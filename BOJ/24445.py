import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
count = 1
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
q = deque([R])

def bfs():
    global count
    visited[R] = count
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for x in graph[v]:
            if visited[x] == 0:
                count += 1
                visited[x] = count
                q.append(x)
                
                
bfs()
for i in range(1, N+1):
    print(visited[i])