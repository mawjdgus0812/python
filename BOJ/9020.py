# import sys
# import itertools

# num = int(sys.stdin.readline())
# for _ in range(num):
#     N = int(sys.stdin.readline())
#     sosu = [2]
#     for i in range(2,N+1):
#         s = 1
#         for j in range(2,i+1):
#             if i % j == 0:
#                 break
#             s += 1
#             if s == (i-1):
#                 sosu.append(i)
#                 break
                
            
#     # print(sosu)
#     perm = itertools.permutations(sosu,2)
#     anw = []
#     if (N / 2) in sosu:
#         print(int(N/2),int(N/2))
#     else:
#         for p in perm:
#             a, b = p
#             # print(a,b)
#             if (a+b) == N and a <= b:
#                 anw.append((a,b))
#         max = 9999

#         for a,b in anw:
#             if b-a < max:
#                 result = (a,b)
#                 max = b-a
#         print(result[0],result[1])

import sys
def is_prime(n):
    if n==1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n%j==0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())
    
    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1