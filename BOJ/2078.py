import sys
INPUT = sys.stdin.readline

A, B = map(int, INPUT().split())
L = R = 0

while A > 1 and B > 1:
  if A > B:
    L += A // B
    A %= B
  else:
    R += B // A
    B %= A
L += A - 1
R += B - 1
print(L, R)

# https://firsteast.tistory.com/m/129