"""
큐 방식인데, 회전한다. 여기서 바로 deque를 써야 한다는 것을 알았는데..
deque 정확한 동작방식을 몰라서 조금 찾아보고 풀었다.
"""

from collections import deque
N,M = map(int,input().split())
position = list(map(int, input().split()))
deq = deque([i+1 for i in range(N)])

count = 0
for i in position:
    while True:
        if i == deq[0]:
            deq.popleft()
            break
        else:
            if deq.index(i) >= len(deq)/2:
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    count += 1
            else:
                while deq[0] != i:
                    deq.append(deq.popleft())
                    count += 1

print(count)