import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('inf')
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

start, end = map(int, input().split())

def dijkstra(start, end):
    dist_arr = [INF]*N
    dist_arr[start-1] = 0
    pq = [(0, start-1)]
    while pq:
        dist, now = heapq.heappop(pq)
        if dist_arr[now] < dist:
            if now == end:
                break
            else: continue

        for next, weight in graph[now]:
            cost = dist + weight
            if cost < dist_arr[next]:
                dist_arr[next] = cost
                heapq.heappush(pq, (cost, next))

    return dist_arr

result = dijkstra(start, end)
print(result[end-1])