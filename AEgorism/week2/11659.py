"""
이거 개쉽잖아?라고 풀었는데 시간초과이다. 왜지
아무래도 시간복잡도에서 걸리는거 같은데 누적합을 저장해놓고 가져다쓰는 방식을 사용해야겠다.
"""

import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

sum_arr = [0]
sums = 0
for num in nums:
    sums += num
    sum_arr.append(sums)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_arr[j]-sum_arr[i-1])