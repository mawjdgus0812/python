import sys
sys.setrecursionlimit(100*100)

N = int(sys.stdin.readline())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
visited_rg = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
cnt_rg = 1
def dfs(x,y):
    global cnt
    if visited[x][y] == 0:
        visited[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == graph[x][y]:
                dfs(nx,ny)

def dfs_rg(x,y):
    global cnt_rg
    if visited_rg[x][y] == 0:
        visited_rg[x][y] = cnt_rg
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == graph[x][y]:
                dfs_rg(nx,ny)
            if graph[nx][ny] in ['R','G'] and graph[x][y] in ['R','G']:
                dfs_rg(nx,ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1
        if visited_rg[i][j] == 0:
            dfs_rg(i,j)
            cnt_rg += 1
            
            
print(cnt-1, cnt_rg-1)