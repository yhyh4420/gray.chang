"""
당연히 브루트포스로 풀면 안되겠지요? 에라토스테네스의 채를 함수로 만들어서 써야겠다.
"""
import math

def eratos(a):
    max_range = 2*a
    is_prime = [True]*(max_range+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(max_range))+1):
        if is_prime[i]:
            for j in range(i*i, max_range+1, i):
                is_prime[j] = False
    count = 0
    for i in range(a+1, max_range+1):
        if is_prime[i]:
            count += 1
    return count
import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(eratos(n))