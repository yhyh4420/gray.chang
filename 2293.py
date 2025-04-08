"""
이건 dp다 좀 에바다 싶으면 손으로 그려보자. 답나옴
"""

import sys

n, k = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort()

dp = [0]*(k+1)
dp[0] = 1
for c in coins:
    for i in range(c, k+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[k])