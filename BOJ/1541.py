import sys

f = sys.stdin.readline().rstrip()

if '-' in f:
    a = f.split('-')
    answer = 0
    for i, cal in enumerate(a):
        if '+' in cal and i == 0:
            answer += sum(map(int,cal.split('+')))
        elif '+' not in cal and i == 0:
            answer += int(cal)
        elif '+' in cal and i != 0:
            answer -= sum(map(int,cal.split('+')))
        elif '+' not in cal and i != 0:
            answer -= int(cal)
            
else:
    a = f.split('+')
    answer = 0
    for cal in a:
        answer += int(cal)
        
        
print(answer)