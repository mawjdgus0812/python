
n, r, c = map(int,input().split())

ans = 0

while n != 0:
    n -= 1
    
    # 1 사분면
    if r < 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0
    
    # 2 사분면
    elif r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 1
        c -= (2**N)
    
    # 3 사분면
    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        r -= (2**N)
    
    # 4 사분면
    else:
        ans += (2**N) * (2**N) * 3
        r -= (2**N)
        c -= (2**N)
print(ans)
    