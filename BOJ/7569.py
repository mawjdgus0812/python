import sys
from collections import deque

N,M,H = map(int, sys.stdin.readline().split())


graph = []
tmp = []
q = deque()
for i in range(H):
    temp = []
    for j in range(M):
        temp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(N):
            if temp[j][k] == 1:
                q.append((k,j,i))
    graph.append(temp)
    
# graph[H][y][x]


# 6 방향
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

# 6 방향 

def bfs():
    while q :
        (x, y, h) = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]
            
            
            if nx < 0 or ny < 0 or nh < 0 or nx >= N or ny >= M or nh >= H:
                continue
            if graph[nh][ny][nx] == 0:
                q.append((nx,ny,nh))
                graph[nh][ny][nx] = graph[h][y][x] + 1

    return graph

bfs()


day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day-1)




