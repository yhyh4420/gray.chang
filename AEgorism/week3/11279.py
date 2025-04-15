"""
추가시간이 없는 것을 보고 그냥 리스트 접근은 힘들겠네..라고 생각헸다.
찾아보니 힙이라는 개념이 있더라..공부해야지
힙을 사용하는 순간 : ~~한 수를 꺼낼 때 / 데이터가 계속 추가되거나 삭제될 때 / 실시간으로 중간값을 구해야 할 때 / 우선순위 큐로 동작해야 할 때
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