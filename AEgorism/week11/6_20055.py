"""
회전하는 큐?
"""
from collections import deque

N, K = map(int, input().split())
container = deque(list(map(int, input().split())))
robot = deque(False for _ in range(N))

count = 0
while True:
    count += 1
    # 먼저 회전하기
    container.rotate(1)
    robot.rotate(1)
    robot[N-1]=False
    # 로봇 이동
    for i in range(N-2,-1,-1):
        if robot[i] and container[i+1] >= 1 and not robot[i+1]:
            container[i+1] -= 1
            robot[i]=False
            robot[i+1]=True
    robot[N-1]=False
    # 로봇 놓기
    if container[0] >= 1:
        container[0] -= 1
        robot[0] = True
    if container.count(0) >= K:
        break
print(count)