##### 내 풀이 #####
import sys

N = int(input())
li = []
names = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    li.append((i, age,name))

# print(li)
li.sort(key=lambda x : (int(x[1]),x[0]))  ## 여기서 lambda쓸 때, int라고 명시해줘야 됨.



for a in li:
    print(a[1]+ " " + a[2])
    
#### 다른 풀이 #####

import sys
arr = sys.stdin.readlines()[1:]
arr.sort(key=lambda x:int(x.split()[0])) 
sys.stdout.write(''.join(arr))