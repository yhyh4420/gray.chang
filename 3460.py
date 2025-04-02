T = int(input())
"""
2씩 나눠서 나머지를 출력하면 됨
"""
def binary(n):
    b_list = []
    count = 0
    while True:
        if n == 0:
            break
        k = n % 2
        n = n // 2
        if k == 1:
            b_list.append(count)
        count += 1
    return b_list

for _ in range(T):
    n = int(input())
    print(*binary(n))