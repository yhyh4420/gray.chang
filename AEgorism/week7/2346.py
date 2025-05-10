"""
인덱스랑 큐를 동시에 가져가면서 풀려고 했는데 메모리 초과가 났다.
deque를 하나만 유지해야 하나..
"""
from collections import deque

N = int(input())
moves = list(map(int, input().split()))
deq = deque((i+1, moves[i]) for i in range(N))

while deq:
    idx, move = deq.popleft()
    print(idx, end=" ")
    if not deq:
        break
    if move > 0:
        deq.rotate(-(move-1))
    else:
        deq.rotate(-move)
# for _ in range(N):
#     if deq[0] > 0:
#         print(idx.popleft(), end=" ")
#         temp = deq.popleft()
#         if not deq:
#             break
#         for _ in range(temp-1):
#             idx.append(idx.popleft())
#             deq.append(deq.popleft())
#     else:
#         print(idx.popleft(), end=" ")
#         temp = deq.popleft()
#         if not deq:
#             break
#         for _ in range(temp*(-1)):
#             idx.appendleft(idx.pop())
#             deq.appendleft(deq.pop())