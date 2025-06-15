"""
소수니까 일단 에라토스테네스의 체를 합시다.
"""

max_int = 1299709

is_prime = [True for _ in range(max_int + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, round(max_int**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, max_int+1, i):
            is_prime[j] = False

def eratos(n):
    if is_prime[n]:
        return 0
    start = n-1
    end = n+1
    while not is_prime[start]:
        start -= 1
    while not is_prime[end]:
        end += 1
    return end-start

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    print(eratos(n))