import sys

N = int(sys.stdin.readline())

dp = [0] * 1000000

dp[0] = 1

if N>=2:
    dp[1] = 2

if N>2:
    for i in range(2,N):
        dp[i] = (dp[i-1] + dp[i-2]) %15746
    
print(dp[N-1])

