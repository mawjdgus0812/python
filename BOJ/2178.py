import queue
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    x,y = 0,0
    
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
    return graph[N-1][M-1]

print(bfs())