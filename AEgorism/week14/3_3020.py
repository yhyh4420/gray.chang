"""
석순이랑 종유석을 분리해서 리스트로 저장하고
그런데 단순 브루트 포스 비교는 시간초과 날 것 같다. O(NxH)인데 N이랑 H가 너무 큼
예전에 풀었던 가장 적게 통나무 자르는 방법이랑 비슷한거 같다. 그런데 리스트 두개로 비교해야 하는..맞나?
그런데 최소 파괴 장애물의 높이는 어쩔 수 없이 완전탐색으로 해줘야 하지 않나..?
"""
import sys
import bisect
input = sys.stdin.readline

N, H = map(int, input().split())
down = []
up = []
for _ in range(N//2):
    down.append(int(input()))
    up.append(int(input()))

down.sort()
up.sort()

MIN = N
count = 0
for h in range(1,H+1):
    down_count = N//2 - bisect.bisect_left(down, h)
    up_count = N//2 - bisect.bisect_left(up, H-h+1)
    total_count = down_count + up_count
    if total_count < MIN:
        MIN = total_count
        count = 1
    elif total_count == MIN:
        count += 1

print(MIN, count)