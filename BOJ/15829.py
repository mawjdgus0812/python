import sys
import string

alpha = list(string.ascii_lowercase)



N = int(input())
sum = 0

a = list(sys.stdin.readline().rstrip())



for i, alphabet in enumerate(a):
    
    sum += (alpha.index(alphabet)+1)*31**i
print(sum)