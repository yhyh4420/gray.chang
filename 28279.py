from collections import deque
import sys

input = sys.stdin.readline

deq = deque()
def function_1(order, X):
    if order == 1:
        deq.appendleft(X)
    elif order == 2:
        deq.append(X)

def function_2(order):
    if order == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif order == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif order == 5:
        print(len(deq))
    elif order == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif order == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif order == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)

N = int(input())
for _ in range(N):
    orders = list(map(int, input().split()))
    if orders[0] == 1 or orders[0] == 2:
        function_1(*orders)
    else:
        function_2(*orders)
