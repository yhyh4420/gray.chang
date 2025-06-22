import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for i in range(N):
    for j in range(N):
        if matrix[i][j] == INF:
            matrix[i][j] = 0
        else: matrix[i][j] = 1

for i in matrix:
    print(*i)