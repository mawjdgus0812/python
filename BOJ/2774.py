import sys

al = list(sys.stdin.readline().rstrip())

for a in al:
    if a.isupper():
        print(a.lower(),end='')
    else:
        print(a.upper(),end='')

print('')