import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
answer = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort(reverse=True)

count = 1
visited = [False] * (N + 1)
stack = [R]
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        answer[node] = count
        count += 1
        for i in graph[node]:
            if not visited[i]:
                stack.append(i)

print(*answer[1:], sep='\n')