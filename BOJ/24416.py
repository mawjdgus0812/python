import sys

def fibo_recursive_func(n):
    global recursive_num
    recursive_num += 1
    if n == 1 or n == 2:
        recursive_num -= 1
        return 1
    else:
        return fibo_recursive_func(n-1) + fibo_recursive_func(n-2)
    
def fibo_dp(n):
    func_exec_num = 0
    fibo_list = [0, 1, 1]
    
    for i in range(3, n+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
        func_exec_num += 1
    return func_exec_num

if __name__ == "__main__":
    n = int(input())
    recursive_num = 0
    
    fibo_recursive_func(n)
    dynamic_num = fibo_dp(n)
    print(recursive_num+1, dynamic_num)