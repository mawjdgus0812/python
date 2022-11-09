import sys

N = int(sys.stdin.readline())
arr=[0]*10000
for i in range(N):
    arr[i]=int(sys.stdin.readline())

dp = [0] * 10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[2] + arr[0], arr[2] + arr[1], dp[1])
for i in range(3, N):
    dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])
print(max(dp))