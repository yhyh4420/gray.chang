import sys
from collections import deque

input = sys.stdin.readline

N, P = map(int, input().split())

guitar = {
    1: deque([0]),
    2: deque([0]),
    3: deque([0]),
    4: deque([0]),
    5: deque([0]),
    6: deque([0])
    }

count = 0
for _ in range(N):
    l,p = map(int, input().split())
    q = guitar[l]
    if p > q[-1]:
        count += 1
        q.append(p)
    elif p < q[-1]:
        while p < q[-1]:
            count += 1
            q.pop()
            if p > q[-1]:
                count += 1
                q.append(p)

print(count)