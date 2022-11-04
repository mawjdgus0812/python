import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
m = []
for _ in range(N):
    m.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        if visited[x][y] == 0:
            visited[x][y] = visited[x][y] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or N <= nx or ny < 0 or ny <= M:
                    continue
                
