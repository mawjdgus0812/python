import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, R = map(int,sys.stdin.readline().split())

visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
count = 1
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

v = deque([R])

def bfs(v):
    global count
    visited[R] = count
    while v:
        u = v.popleft()
        graph[u].sort()
        for x in graph[u]:
            if visited[x] == 0:
                count += 1
                visited[x] = count
                v.append(x)

bfs(v)
for i in range(1, N+1):
    print(visited[i])
                
                
     
