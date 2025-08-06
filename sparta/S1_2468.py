N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

def dfs(rain):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > rain:
                stack = [(i,j)]
                count += 1
                while stack:
                    x,y = stack.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    dx, dy = [-1,1,0,0], [0,0,-1,1]
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if (0<=nx<N and 0<=ny<N) and not visited[nx][ny]:
                            if area[nx][ny] > rain:
                                stack.append((nx, ny))
    return count

max_rain, min_rain = 0, 101
for i in range(N):
    for j in range(N):
        if area[i][j] > max_rain:
            max_rain = area[i][j]
        if area[i][j] < min_rain:
            min_rain = area[i][j]

max_area = 0
for rain in range(min_rain-1, max_rain):
    if max_area < dfs(rain):
        max_area = dfs(rain)
print(max_area)