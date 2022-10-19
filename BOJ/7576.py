import sys
from collections import deque
M, N = map(int,sys.stdin.readline().split())
# M - row
# N - column

graph = []
q = deque()
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)
    for j in range(M):
        if tmp[j] == 1:
            q.append((i,j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    
    (x, y) = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))
            
day = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day,max(i))
    
print(day-1)