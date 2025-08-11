N ,D = map(int, input().split())
shortcut = []
for _ in range(N):
    start, end, dist = map(int, input().split())
    if end <= D:
        shortcut.append((start, end, dist))

dp = [i for i in range(D+1)]
for i in range(1, D+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    for start, end, dist in shortcut:
        dp[end] = min(dp[end], dp[start]+dist)

print(dp[D])