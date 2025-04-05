""""
큐를 사용하는건데..동일한 중요도가 있을 수 있으니 인덱스를 추적하는 방식으로 해야겠다.
"""
import queue

def q(arr, idx):
    count = 1
    while True:
        if max(arr) != arr[0]:
            temp = arr[0]
            arr.pop(0)
            arr.append(temp)
            if idx == 0:
                idx = len(arr)-1
            else: idx -= 1
        else:
            if idx == 0:
                break
            else:
                arr.pop(0)
                count += 1
                idx -= 1

    return count

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    print(q(importance, M))
