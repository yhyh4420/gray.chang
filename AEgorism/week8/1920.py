N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
find_arr = list(map(int, input().split()))

def find(i):
    start = 0
    end = N-1
    is_find = False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == i:
            is_find = True
            print(1)
            return
        if A[mid] > i:
            end = mid-1
        if A[mid] < i:
            start = mid+1
    if not is_find:
        print(0)
        return

for i in find_arr:
    find(i)