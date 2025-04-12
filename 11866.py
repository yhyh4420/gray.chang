from collections import deque

N, K = map(int, input().split())

deq = deque(list(i+1 for i in range(N)))
answer = []
count = 0
while deq:
    count += 1
    if count % K == 0:
        i = deq.popleft()
        answer.append(i)
    else:
        i = deq.popleft()
        deq.append(i)

print("<", end="")
for i in range(N-1):
    print(answer[i], end=", ")
print(answer[-1], end="")
print(">", end="")
