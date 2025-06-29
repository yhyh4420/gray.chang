"""
반드시 추월을 한다는 전제 : 순서가 유지되지 않음
첫번째 차는 추월할 곳이 없음. 그니까 첫번째를 기준으로 삼으면 됨
1번을 기준으로 증가하는 수열을 찾고 N에서 그 값을 빼면 될 듯
"""

import sys
input = sys.stdin.readline

N = int(input())
tunnel_in = [input() for _ in range(N)]
tunnel_out = [input() for _ in range(N)]

count = 0
idx = -1
for i in tunnel_in:
    out = tunnel_out.index(i)
    if out > idx:
        idx = out
        count += 1

print(N-count)
