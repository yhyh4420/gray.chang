from collections import deque

N, M = map(int, input().split())

map_arr = []
for _ in range(N):
    map_arr.append(input())

q = deque()
def bfs():
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]
    visited = []
    count = 1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        visited.append((x, y))
        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if 0 <= dx < N and 0 <= dy < M and map_arr[dy][dx] == 1:
                count += 1
                if (dx, dy) not in visited:
                    q.append((dx, dy))
    return count

print(bfs())