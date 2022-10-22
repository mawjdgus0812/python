import sys


N, M = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))

sum_list = [0]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
    sum_list.append(total)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])