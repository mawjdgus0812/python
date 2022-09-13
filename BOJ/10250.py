##### 내 풀이 #####
import sys

T = int(input())

for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    height = 0
    width = 0
    if N % H == 0:
        height = H
        width = N // H
    else:
        height = N % H
        width = N // H + 1
    print(height * 100 + width)
                                
##### 1등 풀이 #####
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    h,w,n = map(int,input().split())
    print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0')) 