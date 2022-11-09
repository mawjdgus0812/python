import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr_reverse = arr[::-1]
dp = [0] * N
dp_reverse = [0] * N
dp[0] = 1
dp_reverse[0] = 1

def dynamic(dp,arr):
    for i in range(1,N):
        m = 0
        for j in range(i):
            if arr[i] > arr[j]:
                m = max(dp[j],m)
            dp[i] = m+1
    return dp

dp = dynamic(dp,arr)
dp_reverse = dynamic(dp_reverse,arr_reverse)
sum = [x + y for (x,y) in zip(dp,dp_reverse[::-1])]
print(max(sum)-1)