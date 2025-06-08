import sys
from collections import deque

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

"""
그래프 탐색 국룰
1. bfs는 큐, dfs는 스택
2. 방문 여부 확인하는 자료구조(실제 문제와 동일한 자료구조)
3. 방문 횟수같은거 기록할 자료구조(실제 문제와 동일한 자료구조)
4. 시작 위치를 큐 or 스택에 넣고 방문했다고 기록
5. while문 on
6. 큐 or 스택에서 pop하고 검증, 검증되면 리턴하고 끝
7. 검증 실패하면 pop한 장소에서 갈 수 있는 다른 장소를 큐에 넣고 방문했다고 기록, 방문 횟수에 추가
"""
def bfs(i, start, target):
    queue = deque()
    visited = [[False] * i for _ in range(i)]
    matrix = [[0]*i for _ in range(i)]
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        if x == target[0] and y == target[1]:
            return matrix[x][y]
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<i and 0<=ny<i and not visited[nx][ny]:
                visited[nx][ny] = True
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    d = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    print(bfs(d, start, target))