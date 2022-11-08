import sys


arr = []
dp = []

l = int(sys.stdin.readline())
for _ in range(l):
    arr.append(int(sys.stdin.readline()))
    
dp.append(arr[0])
if l == 2:
    dp.append(max(arr[0]+arr[1],arr[1]))

if l >= 3:
    dp.append(max(arr[0]+arr[1],arr[1]))
    dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))

if l >= 3:
    for i in range(3, l):
        dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]))
    
print(dp.pop())

