N = int(input())
array = list(map(int, input().split()))

dp = array[:]

for i in range(N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))