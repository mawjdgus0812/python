##### 내 풀이 #####
import sys

N = int(input())

cards = list(map(int,sys.stdin.readline().split()))

M = int(input())

how = list(map(int, sys.stdin.readline().split()))
dic = {i:0 for i in cards}

for i in cards:
    dic[i] += 1
    
for i in how:
    if i in dic.keys(): ## 그냥 리스트보다 훨씬 빠름
        print(dic[i],end=' ')
    else:
        print(0, end=' ')
        
        
##### 다른 풀이 #####

import sys
from collections import Counter

input = sys.stdin.readline
input()
card = Counter(input().split())
print(card)
input()
cmp = [card[i] for i in input().split()]
print(' '.join(map(str, cmp)))


#######

import sys
stdin = sys.stdin.read().splitlines()
A = map(int,stdin[1].split())
B = map(int,stdin[3].split())
dic = {}
for n in A:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
print(' '.join(str(dic[n]) if n in dic else '0' for n in B))