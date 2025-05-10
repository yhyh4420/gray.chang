from collections import deque

stack = deque()
def function_1(order, X):
    if order == 1:
        stack.append(X)

def function_2(order):
    if order == 2:
        if stack:
            print(stack.pop())
        else: print(-1)
    elif order == 3:
        print(len(stack))
    elif order == 4:
        if stack:
            print(0)
        else: print(1)
    elif order == 5:
        if stack:
            print(stack[len(stack) - 1])
        else: print(-1)

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    orders = list(map(int, input().split()))
    if orders[0] == 1:
        function_1(orders[0], orders[1])
    else:
        function_2(orders[0])
