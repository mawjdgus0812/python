import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]


for _ in range(M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    count = 1
    q = deque([1])
    
    visited[1] = count
    while q:
        v = q.popleft()
        for x in graph[v]:
            if visited[x] == 0:
                visited[x] = count
                q.append(x)
                
bfs()

print(sum(visited)-1)