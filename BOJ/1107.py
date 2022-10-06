
import sys

target = int(sys.stdin.readline())

N = int(sys.stdin.readline())

broken = list(map(int,sys.stdin.readline().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        
        elif j == len(nums) - 1:
            min_count = min(min_count , abs(int(nums) - target) + len(nums))
            
print(min_count)