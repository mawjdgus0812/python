import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

dp = [0] * (N)
dp[0] = 0

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))