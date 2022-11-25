import sys

while True:
    N,M = map(int,sys.stdin.readline().split())
    if N == M == 0:
        break
    if M % N == 0:
        print('factor')
    elif N % M == 0:
        print('multiple')
    else:
        print('neither')
    
    