import sys
import heapq
input = sys.stdin.readline

N = int(input())
due_score = []
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(due_score, (-w, d))
answer = [0]*1001

while due_score:
    w, d = heapq.heappop(due_score)
    w = -w
    if answer[d] == 0:
        answer[d] = w
    else:
        while d != 0:
            d -= 1
            if answer[d] == 0:
                answer[d] = w
                break

print(sum(answer[1:]))