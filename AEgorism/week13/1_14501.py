import sys

input = sys.stdin.readline
N = int(input())
counsel = []
for _ in range(N):
    counsel.append(list(map(int, input().split())))

dp = [0]*(N+1)

# for i in range(N-1, -1, -1):
#     if i + counsel[i][0] <= N:
#         dp[i] = max(dp[i+1], dp[i+counsel[i][0]] + counsel[i][1])
#     else:
#         dp[i] = dp[i+1]

for i in range(N):
    for j in range(i+counsel[i][0], N+1):
        dp[j] = max(dp[j], dp[i] + counsel[i][1])

print(max(dp))