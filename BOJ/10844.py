import sys

N = int(sys.stdin.readline())
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
dp = [[0]*10 for _ in range(101)]
dp[0][0] = 0
for i in range(1,10):
    dp[0][i] = 1

for i in range(1,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1])%1000000000)


# import sys

# N = int(sys.stdin.readline())
# # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# dp = [[0]*10 for _ in range(101)]
# dp[0][0] = 0
# for i in range(1,10):
#     dp[0][i] = 1

# for i in range(1,N+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][0] = (dp[i-1][1]%1000000000)
#         elif j == 9:
#             dp[i][9] = (dp[i-1][8]%1000000000)
#         else:
#             dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000

# print(sum(dp[N-1]))
