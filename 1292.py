a,b = map(int,input().split())

arr = []
for i in range(1,1001):
    for _ in range(i):
        arr.append(i)

print(sum(arr[a-1:b]))