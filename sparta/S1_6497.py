N = int(input())

dp = [[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    R,G,B = map(int, input().split())
    dp[i][0] = R + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = G + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = B + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N]))