N = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibo_arr = [fibonacci(n) for n in range(21)]
print(fibo_arr[N])