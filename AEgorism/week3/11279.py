"""
추가시간이 없는 것을 보고 그냥 리스트 접근은 힘들겠네..라고 생각헸다.
"""

import heapq
import sys

input = sys.stdin.readline
N = int(input())
arr = []
heapq.heapify(arr)
for _ in range(N):
    n = int(input())
    if n == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (-n, n))