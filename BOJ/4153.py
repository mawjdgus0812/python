##### 내 풀이 #####

import sys


while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a == b == c == 0:
        break
    if c**2 == (b**2 + a**2) or a**2 == (b**2 + c**2) or b**2 == (a**2+c**2):
        print('right')
    else:
        print('wrong')


##### 1등 풀이 #####

while True:
    num = list(map(int,input().split()))
    max_num = max(num)

    if max_num ==0:
        break
    
    num.remove(max_num)
    if max_num**2==num[0]**2+num[1]**2:
            print("right")
    else:
        print("wrong")

