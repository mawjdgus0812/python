import sys


import sys
from collections import deque


N, M = map(int,sys.stdin.readline().split())
graph = []
graph.append([1 for _ in range(M+2)])
for _ in range(N):
    graph.append([1]+list(map(int,sys.stdin.readline().split()))+[1])
graph.append([1 for _ in range(M+2)])
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

for i in range(1,N+1):
    for j in range(1,M+1):
        if graph[i][j] == 2:
            q.append((i,j))
print(q)

while q:
    (x, y) = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < N+2 and ny >= 0 and ny < M+2:
            if graph[nx][ny] == 1:
                continue
            elif graph[nx][ny]==0:
                # print(nx,ny)
                q.append((nx,ny))
                graph[nx][ny] = 2
            
            
print(graph)
###

# from collections import deque
# import copy

# def bfs():
#     queue = deque()
#     tmp_graph = copy.deepcopy(graph)
#     for i in range(n):
#         for j in range(m):
#             if tmp_graph[i][j] == 2:
#                 queue.append((i, j))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if tmp_graph[nx][ny] == 0:
#                 tmp_graph[nx][ny] = 2
#                 queue.append((nx, ny))

#     global answer
#     cnt = 0

#     for i in range(n):
#         cnt += tmp_graph[i].count(0)

#     answer = max(answer, cnt)


# def makeWall(cnt):
#     if cnt == 3:
#         bfs()
#         return

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 makeWall(cnt+1)
#                 graph[i][j] = 0

# n, m = map(int, input().split())
# graph = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# answer = 0
# makeWall(0)
# print(answer)