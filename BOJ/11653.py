

import sys

N = int(sys.stdin.readline())

for i in range(2,N+1):
    while True:
        if N % i == 0:
            print(i)
            N /= i
        else:
            break


