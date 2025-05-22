import heapq

INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(graph, start):
    dist_arr = [INF] * (N + 1)
    dist_arr[start] = 0
    pq = [(0, start)]
    while pq:
        distance, now = heapq.heappop(pq)
        if distance > dist_arr[now]:
            continue
        for next, weight in graph[now]:
            cost = distance + weight
            if cost < dist_arr[next]:
                dist_arr[next] = cost
                heapq.heappush(pq, (cost, next))

    return sum(dist_arr[1:])

min_total = INF
answer = 0

for i in range(1, N + 1):
    total = dijkstra(graph, i)
    if total < min_total:
        min_total = total
        answer = i

print(answer)