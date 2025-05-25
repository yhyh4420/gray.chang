import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
sums = 0
for i in range(N):
    sums += arr[i]
    sum_arr.append(sums)

answer = -sys.maxsize
for i in range(K, N+1):
    answer = max(answer, sum_arr[i] - sum_arr[i - K])

print(answer)