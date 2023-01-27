import sys

n = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))

if len(nums) > 1:
    nums.sort()
    print(nums[0]*nums[-1])
else:
    print(nums[0]**2)

