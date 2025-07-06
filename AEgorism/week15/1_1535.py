N = int(input())
damage = list(map(int, input().split()))
happy = list(map(int, input().split()))

# dp = [0] * 101

# for i in range(N):
#     next_dp = dp[:]
#     for hp in range(damage[i],101):
#         next_dp[hp] = max(dp[hp], dp[hp-damage[i]] + happy[i])
#     dp = next_dp

# print(dp[99])

dp = [[0] * 101 for _ in range(N+1)]
for i in range(1,N+1):
    for hp in range(1,101):
        if hp > damage[i-1]:
            dp[i][hp] = max(dp[i-1][hp], dp[i-1][hp-damage[i-1]] + happy[i-1])
        else:
            dp[i][hp] = dp[i-1][hp]


print(max(dp[N][1:]))