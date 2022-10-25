import sys
from tkinter import N

X = int(sys.stdin.readline())
line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    num1 = X
    num2 = line - X + 1
elif line % 2 == 1:
    num1 = line - X + 1
    num2 = X
print(num1, "/",num2, sep = "")
# 1 : 1/1

# 2 : 1/2 2/1

# 3 : 3/1 2/2 1/3

# 4 : 1/4 2/3 3/2 4/1

# 5 : 5/1 4/2 3/3 2/4 1/5

