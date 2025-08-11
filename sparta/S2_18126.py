N = int(input())
graph = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    A,B,C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

stack = [1]
dist = [float('inf')]*(N+1)
dist[1] = 0
visited = [False]*(N+1)

while stack:
    current_node = stack.pop()
    if visited[current_node]:
        continue
    visited[current_node] = True
    for neighbor, distence in graph[current_node]:
        if dist[neighbor] > dist[current_node] + distence:
            dist[neighbor] = dist[current_node] + distence
            stack.append(neighbor)

print(max(dist[1:]))