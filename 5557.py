# """
# 백트래킹으로 될거같다.
# """
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# count = 0
# def back(n, answer):
#     global count
#     """
#     마지막 두 숫자 사이에 =를 넣고 등식을 만드는거임
#     """
#     if n == N-1:
#         if answer == arr[-1]:
#             count += 1
#         return
#     if 0 <= answer + arr[n] <= 20:
#         back(n + 1, answer + arr[n])
#     if 0 <= answer - arr[n] <= 20:
#         back(n + 1, answer - arr[n])
#
# back(1, arr[0])
# print(count)

"""
백트래킹으로 답은 나오는데 시간초과..
찾아보니까 디피네..
"""

N = int(input())
arr = list(map(int, input().split()))

dp = [[0]*21 for _ in range(N-1)]
dp[0][arr[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i-1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i-1][j]

print(dp[N-2][arr[-1]])