

##### 내 풀이 #####

N = int(input())
tmp = [[0 for _ in range(14)] for _ in range(15)]
tmp[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


for i in range(14):
    for j in range(14):
        tmp[i+1][j] = sum(tmp[i][:j+1])

for _ in range(N):
    K = int(input())
    N = int(input())
    print(tmp[K][N-1])
    
    
##### 1등 풀이 #####

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])
    


