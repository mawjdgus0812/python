import sys
import math
M = 1
while True:
    sosu_sum = 0
    M = int(sys.stdin.readline())
    if M == 0:
        break
    for i in range(M,M*2+1):
        sosu = 1
        if i == M:
            continue
        if i == 2:
            sosu_sum += 1
            continue
        if i > 1:
            a = int(math.sqrt(i))+2
            for j in range(2,a):
                # print(i, j)
                if i % j == 0:
                    sosu = 0
                    break
                else:
                    continue
            if sosu == 1:
                sosu_sum += 1
                # print(i)
        else:
            continue
        
    print(sosu_sum)
        
    