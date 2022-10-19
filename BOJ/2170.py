import sys


N = int(sys.stdin.readline())
origin_lines = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))

origin_lines.sort()

start = origin_lines[0][0]
end = origin_lines[0][1]

ans = 0
for i in range(1, N):
    now_start, now_end = origin_lines[i]
    
    # 겹치는 경우
    if end > now_start:
        end = max(end, now_end)
        
    # 안겹치는 경우
    else:
        ans += (end - start)
        start, end = now_start, now_end
ans += (end - start)
print(ans)