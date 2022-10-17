import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())
count = 1
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(R):
    global count
    visited[R] = count
    graph[R].sort(reverse=True)
    for x in graph[R]:
        if visited[x] == 0:
            count += 1
            dfs(x)

dfs(R)

for i in range(1,N+1):
    print(visited[i])
            