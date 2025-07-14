import sys

input = sys.stdin.readline

N,K = map(int, input().split())
bag = [[0,0]]
for _ in range(N):
    W,V = map(int, input().split())
    bag.append([W,V])


dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        w,v = bag[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])

print(dp[N][K])