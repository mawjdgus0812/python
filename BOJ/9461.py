import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * (N+1)
    dp[1] = 1
    if N > 1:
        dp[2] = 1
    if N > 2:
        dp[3] = 1
    if N > 3:
        for i in range(4,N+1):
            dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[-1])

