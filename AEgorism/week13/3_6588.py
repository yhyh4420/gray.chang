import sys
input = sys.stdin.readline

max_int = 1000000

is_prime = [True] * max_int
is_prime[0] = False
is_prime[1] = False
prime = []
for i in range(2, int(max_int**0.5)):
    if is_prime[i]:
        for j in range(i*2, max_int, i):
            is_prime[j] = False
for i in range(3, max_int):
    if is_prime[i]:
        prime.append(i)

def goldbach(n):
    for i in prime:
        if is_prime[n - i]:
            a = i
            b = n - i
            print(f"{n} = {a} + {b}")
            break
        if i > n//2:
            print("Goldbach's conjecture is wrong")
            break

while True:
    n = int(input())
    if n == 0:
        break
    goldbach(n)
