"""
이진 탐색 트리로 하면 될 듯? 구현 방법은 조금 더 생각해봐야겠다.
"""
import sys
N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
find = list(map(int, sys.stdin.readline().split()))

def find_start(arr, target):
    start, end = 0, N
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def find_end(arr, target):
    start, end = 0, N
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

for i in find:
    print(find_end(cards, i)-find_start(cards, i), end=" ")