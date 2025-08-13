def dfs(w,h,area):
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and area[i][j] == 1:
                stack = [(i,j)]
                count += 1
                while stack:
                    x,y = stack.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    dx, dy = [-1,1,0,0,1,1,-1,-1], [0,0,-1,1,1,-1,1,-1]
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if (0<=nx<h) and (0<=ny<w) and not visited[nx][ny]:
                            if area[nx][ny] == 1:
                                stack.append((nx, ny))
    return count

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    area = []
    for _ in range(h):
        area.append(list(map(int, input().split())))
    print(dfs(w,h,area))