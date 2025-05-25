N, K = map(int, input().split())

arr = [i+2 for i in range(N-1)]
answer = []

for i in range(2, N+1):
    for item in arr:
        if item % i == 0:
            answer.append(item)
            arr.remove(item)

print(answer[K-1])