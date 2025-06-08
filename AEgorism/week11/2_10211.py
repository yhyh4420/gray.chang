import sys

def maximum_subarray_sum(arr):
    sum_arr = [0]
    for num in arr:
        sum_arr.append(sum_arr[-1] + num)
    max_sum = -sys.maxsize
    for i in range(len(sum_arr)):
        for j in range(i + 1, len(sum_arr)):
            max_sum = max(max_sum, sum_arr[j] - sum_arr[i])
    return max_sum

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(maximum_subarray_sum(arr))