import sys

N, K = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))

num_list = []
num_list.append(sum(numbers[:K]))

for i in range(N-K):
    num_list.append(num_list[i] - numbers[i] + numbers[i+K])

print(max(num_list))

