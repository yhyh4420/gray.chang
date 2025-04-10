import sys

input = sys.stdin.readline

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
INF = 10 ** 6
dp = [INF]*(k+1)
dp[0] = 0
for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])