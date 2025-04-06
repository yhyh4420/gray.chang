from collections import deque
import sys
N = int(input())

q = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        command[1] = int(command[1])
        q.append(command[1])
    if command[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    if command[0] == "size":
        print(len(q))
    if command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    if command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    if command[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)