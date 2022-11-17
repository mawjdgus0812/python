import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sosu_min = 0
sosu_sum = 0

for i in range(M,N+1):
    sosu = 1
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                sosu = 0
                break
            else:
                continue
        if sosu == 1 and sosu_min ==0:
            sosu_min = i
        if sosu == 1:
            sosu_sum += i
                
    else:
        continue
if sosu_min ==0 and sosu_sum ==0:
    print(-1)
else:
    print(sosu_sum)
    print(sosu_min)

