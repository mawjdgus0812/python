import sys

while True:
    a = list(sys.stdin.readline().rstrip())
    if a == ['.']:
        break
    test = []
    print(a)
    sum=1
    for i in a:
        try:
            if '(' == i:
                test.append(i)
            if '[' == i:
                test.append(i)
            
            if ')' == i:
                if '(' != test.pop():
                    sum = 0 
                    break
            
            if ']' == i:
                if '[' != test.pop():
                    sum = 0
                    break
                
        except:
            sum = 0
            break
        
    if len(test) == 0 and sum==1:
        print('yes')
    else:
        print('no')

        