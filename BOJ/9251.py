import sys

# 1. 2차원 배열의 캐시를 만들어서 해결 가능
# 2. 누적 값으로 가능
arr = list(sys.stdin.readline().rstrip())
arr2 = list(sys.stdin.readline().rstrip())

for i in arr:
    for j in arr2:
        