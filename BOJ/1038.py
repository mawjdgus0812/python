
N = int(input())
answer = 0
for i in range(1000000001):
    # print(answer)
    max = 10
    con = i
    tem = 0
    for j in str(con):
        # print(j)
        if int(j) < max:
            max = int(j)
            continue
        else:
            tem = 1
            break
    
    if answer == N and tem == 0:
        print(con)
        break
    
    if tem == 0:
        answer += 1
    
if i > 9876543210:
    print(-1)