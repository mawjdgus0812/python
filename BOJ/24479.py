import sys
sys.setrecursionlimit(10**9)

N, M, R = map(int,sys.stdin.readline().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
count = 1
for _ in range(M):
    V, E = map(int,sys.stdin.readline().split())
    graph[V].append(E)
    graph[E].append(V)
    

def dfs(s):
    global count
    visited[s] = count
    graph[s].sort()
    for x in graph[s]:
        if visited[x] == 0: 
            count += 1
            dfs(x)
        
dfs(R)

for i in range(1, N+1):
    print(visited[i])
        
        





    