import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    dist = [[int(1e9)] * m for _ in range(n)]
    dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] != int(1e9):
                continue
            
            dist[nx][ny] = dist[x][y] + 1
            if graph[nx][ny] == 0:
                q.append((nx, ny))
    return dist

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dist_start = bfs(0, 0)
dist_end = bfs(n - 1, m - 1)

ans = dist_start[n - 1][m - 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = min(ans, dist_start[i][j] + dist_end[i][j])

print(-1 if ans == int(1e9) else ans + 1)


import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 체크를 2가지 케이스로 나눠서 진행해야함
# [0, 0] : 지나지않은케이스, 벽을 지나온케이스
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]


def bfs():
    # 큐: x, y, 벽을 뚫었는지 여부 (1이면 이제 벽 못뚫음.)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 비용

    while queue:
        x, y, flag = queue.pop()

        # 여기가 이슈임. 무작정 방문했다고 컨티뉴 날려버리면안됨. 두가지 경우로 나눠야함.
        # if visited[x][y] == 1:
        #     continue

        if x == N - 1 and y == M - 1:
            return visited[x][y][flag]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 뚫여있고, 아직 방문하지 않은 상태
                if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    queue.appendleft((nx, ny, flag))
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                # 벽이 막혀있는 상태
                elif graph[nx][ny] == 1 and flag == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][flag] + 1

    return -1


print(bfs())