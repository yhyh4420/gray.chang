import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [0]*N
for i in range(N):
    times[i] = int(input())

start = 1
end = max(times) * M
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for time in times:
        sum += (mid // time)
    if sum >= M:
        end = mid-1
    else:
        start = mid+1

print(start)