N = int(input())
weights = list(map(int, input().split()))

target = 1
for weight in weights:
    if weight >= target:
        print(target)
        break
    target += weight
