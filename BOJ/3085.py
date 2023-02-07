
import sys
import copy

N = int(sys.stdin.readline())
b = []
for _ in range(N):
    b.append(list(sys.stdin.readline().rstrip()))

def count(data):
    Max = 1
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if data[i][j] == data[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)
        cnt = 1
        for j in range(N-1):
            if data[j][i] == data[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)
    return Max
ans = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            move = copy.deepcopy(b)
            move[i][j+1] = b[i][j]
            move[i][j] = b[i][j+1]
            temp = count(move)
            ans = max(ans, temp)
            
        if i+1 < N:
            move = copy.deepcopy(b)
            move[i+1][j] = b[i][j]
            move[i][j] = b[i+1][j]
            temp = count(move)
            ans = max(ans, temp)
print(ans)
        
