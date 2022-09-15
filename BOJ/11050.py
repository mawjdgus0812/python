##### 내 풀이 #####

# from itertools import combinations

# N, K = map(int,input().split())
# combination = list(combinations(range(N),K))
# print(len(combination))

N, K = map(int, input().split())

N_factorial = 1
K_factorial = 1

for i in range(1,K+1):
    K_factorial*=i
    
for i in range(N-K+1,N+1):
    N_factorial*=i


print(int(N_factorial/K_factorial))

##### 1등 풀이 #####
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

ans = 1
for i in range(n, n-k, -1):
    ans *= i

for i in range(1, k+1):
    ans //= i
print(ans)