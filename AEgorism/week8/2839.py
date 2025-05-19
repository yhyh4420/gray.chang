N = int(input())
dp = [0] * (N+1)
for i in range(N+1):
    if i%3 == 0:
        dp[i] = i//3
    if i%5 == 0:
        dp[i] = i//5

for i in range(3,N+1):
    if dp[i-3] != 0 and dp[i-5] != 0:
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])