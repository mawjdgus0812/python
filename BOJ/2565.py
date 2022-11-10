import sys

N = int(sys.stdin.readline())
arr_A =[0 for i in range(1,501)]
arr_B = [0 for i in range(1,501)]
dp_A = [0] * 101
dp_B = [0] * 101
dp_C = [0] * 101
dp_D = [0] * 101
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    arr_A[A] = B
    arr_B[B] = A




def dynamic(dp,arr):
    for i in range(1,101):
        for j in range(1,i+1):
            if arr[i] == 0:
                break
            if arr[i] < arr[j]:
                dp[i] = 1
                break
                
    return dp
def dynamic_B(dp,arr):
    for i in range(1,101):
        for j in range(1,i+1):
            if arr[i] == 0:
                break
            if arr[i] > arr[j]:
                dp[i] = 1
                break
                
    return dp

print(min(sum(dynamic(dp_A,arr_A)),sum(dynamic(dp_B,arr_B)),sum(dynamic_B(dp_C,arr_A)),sum(dynamic_B(dp_D,arr_B))))