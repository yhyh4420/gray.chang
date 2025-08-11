N = int(input())

dp = [[0]*10 for _ in range(N+1)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,N):
    for j in range(10):
        dp[i+1][j] = sum(dp[i][j:]) % 10007
print(sum(dp[N]) % 10007)