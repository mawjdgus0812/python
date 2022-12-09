import sys

N, M = map(int,sys.stdin.readline().split())
result = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(2):
    for i in range(N):
        a = list(map(int,sys.stdin.readline().split()))
        for j in range(M):
            result[i][j] += a[j]
        
for i in range(N):
    for j in range(M):
        print(result[i][j],end=' ')
    print('')
        
        

        
    