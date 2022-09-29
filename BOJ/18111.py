import sys

N, M, B = map(int,sys.stdin.readline().split())
mmap = []
for _ in range(N):
    mmap.append(list(map(int,sys.stdin.readline().split())))
    
answer = sys.maxsize
mmax = 0
for i in range(257):
    max_tg, min_tg = 0, 0
    
    for j in range(N):
        for k in range(M):
            if mmap[j][k] >= i:
                max_tg += mmap[j][k]-i
            else:
                min_tg += i-mmap[j][k]
            
    
    if max_tg + B >= min_tg:
        if min_tg + (max_tg * 2) <= answer:
            answer = min_tg + (max_tg*2)
            mmax = i

            
print(answer, max)
            
    