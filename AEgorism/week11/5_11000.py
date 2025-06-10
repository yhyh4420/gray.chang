import heapq
import sys

input = sys.stdin.readline
N = int(input())
study = [list(map(int, input().split())) for _ in range(N)]
study.sort()

heap = []
heapq.heappush(heap, study[0][1])
for i in range(1,N):
    if study[i][0] < heap[0]:
        heapq.heappush(heap, study[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, study[i][1])

print(len(heap))