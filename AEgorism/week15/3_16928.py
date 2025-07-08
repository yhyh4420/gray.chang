from collections import deque

N,M = map(int, input().split())
map_info = [0]*101
for _ in range(N+M):
    start, end = map(int, input().split())
    map_info[start] = end
visited=[False]*101
"""
이웃 노드는 무조건 자기+주사위 굴린것 map_info의 값이다.
"""
def bfs():
    start = 1
    q = deque()
    q.append((start, 0))
    while q:
        pos, count = q.popleft()
        if pos == 100:
            return count
        for i in range(1,7):
            next_pos = pos+i
            if next_pos > 100:
                continue
            if map_info[next_pos] != 0:
                next_pos = map_info[next_pos]
            if not visited[next_pos]:
                q.append((next_pos, count+1))
                visited[next_pos] = True


answer = bfs()
print(answer)