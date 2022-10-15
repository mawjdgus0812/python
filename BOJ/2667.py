### bfs ###

# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)

# N = int(sys.stdin.readline())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# graph = []


# for i in range(N):
#     graph.append(list(map(int,sys.stdin.readline().rstrip())))
    
# def bfs(graph, x, y):
    
#     queue = deque()
#     queue.append((x,y))
#     graph[x][y] = 0
#     cnt = 1
    
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
            
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx,ny))
#                 cnt += 1
    
#     return cnt

# count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]
# count.sort()
# print(len(count))
# for i in count:
#     print(i)


### dfs ###

import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

def dfs(x,y):
    
    global cnt
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >=0 and ny < N:
                dfs(nx, ny)
                # cnt = 0
    return cnt

count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(dfs(i,j))
            cnt = 0
print(len(count))
count.sort()
for i in count:
    print(i)
