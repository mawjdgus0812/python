import sys

N = int(sys.stdin.readline())
arr = []
dp = [0] * 101

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    arr.append((A,B))
arr.sort(key=lambda x : x[0])

for i in range(len(arr)):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] = dp[i] + 1
print(N-max(dp))