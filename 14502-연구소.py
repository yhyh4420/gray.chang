import itertools
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

"""
일단 0이 최대 64개가 있을 수 있으니까 3개 뽑는건 복잡도가 크지 않을 것 같다.
3개 뽑은 맵에 대해서 bfs를 돌리고 최대값을 갱신하면 될듯?
"""
"""
이방법은 로직은 맞는거 확인했는데 시간초과가 난다. 완전탐색으로 벽 세우면 안되나부다
벽을 어떻게 세울지도 고민해야 할 듯
"""
# zero_list = [[i, j] for i in range(N) for j in range(M) if lab[i][j] == 0]
# zero_select = list(itertools.combinations(zero_list, 3))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs(grid):
#     two_list = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 2]
#     for virus in two_list:
#         visited = set()
#         deq = deque([virus])
#         while deq:
#             (i, j) = deq.popleft()
#             grid[i][j] = 2
#             visited.add((i, j))
#             for d in range(4):
#                 if 0 <= i+dx[d] < N and 0 <= j+dy[d] < M:
#                     if grid[i+dx[d]][j+dy[d]] == 0:
#                         if (i+dx[d], j+dy[d]) not in visited:
#                             deq.append((i+dx[d], j+dy[d]))
#     count = 0
#     for i in grid:
#         for j in i:
#             if j == 0:
#                 count += 1
#     return count
#
# answer = 0
# for zero_xy in zero_select:
#     lab_copy = [row[:] for row in lab]
#     for x, y in zero_xy:
#         lab_copy[x][y] = 1
#     answer = max(answer, bfs(lab_copy))
#
# print(answer)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
def bfs():
    lab_copy = [row[:] for row in lab]
    q = deque()
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 2:
                q.appendleft((i, j))
    while q:
        i, j = q.popleft()
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < N and 0 <= ny < M and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                q.append((nx, ny))
    global answer
    count = 0
    for row in lab_copy:
        count += row.count(0)
    answer = max(answer, count)

def backtrack(wall):
    if wall == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                backtrack(wall+1)
                lab[i][j] = 0

backtrack(0)
print(answer)