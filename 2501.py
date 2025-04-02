N, K = map(int, input().split())

lists = []
for i in range (1, N+1):
    if N % i == 0:
        lists.append(i)

if K > len(lists):
    print(0)
else:
    print(lists[K-1])