
N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])

#################

import sys

N = int(sys.stdin.readline())
cache = {1:0, 2:1}

def dp(n):
    if n in cache:
        return cache[n]

    cache[n] = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    return cache[n]