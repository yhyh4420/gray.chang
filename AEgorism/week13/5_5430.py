from collections import deque
from itertools import groupby

def solution(order_original, length, array):
    if order_original.count("D") > length:
        return "error"
    is_reverse = True # 마지막에 배열 거꾸로 할건지 아닌지
    if order_original.count("R") % 2 == 0:
        is_reverse = False
    order_list = deque((char, len(list(group))) for char, group in groupby(order_original))
    front = True # 앞에서 뽑을지 뒤에서 뽑을지
    while order_list:
        char, count = order_list.popleft()
        if char == "D": # 뽑는 연산의 경우
            if front:
                for _ in range(count):
                    array.popleft()
            else:
                for _ in range(count):
                    array.pop()
        elif count % 2 != 0:
            front = not front
    if is_reverse:
        array.reverse()
        return array
    else:
        return array

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    order = input().rstrip()
    length = int(input())
    array_input = input().rstrip()
    if array_input == "[]":
        array = deque()
    else:
        array = deque(map(int, array_input[1:-1].split(",")))
    answer = solution(order, length, array)
    if answer == "error":
        print("error")
    else:
        print("[", end="")
        print(",".join(map(str, answer)), end="")
        print("]",)