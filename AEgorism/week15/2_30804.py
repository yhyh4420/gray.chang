from collections import defaultdict
import sys

N = int(input())
q = list(map(int, input().split()))

# sys.setrecursionlimit(10**9)
# answer = 0
# def back():
#     global answer
#     if len(set(q)) <= 2:
#         answer = max(answer, len(q))
#         return
#     temp = q.popleft()
#     back()
#     q.appendleft(temp)
#     q.pop()
#     back()

# back()
# print(answer)

answer = 0
count = defaultdict(int)
start = 0
for end in range(N):
    count[q[end]] += 1
    while len(count) > 2:
        count[q[start]] -= 1
        if count[q[start]] == 0:
            del count[q[start]]
        start += 1
    answer = max(answer, end-start+1)

print(answer)