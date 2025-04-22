import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u-1].append((v-1, w))

def dijkstra(start):
    dist_arr = [INF] * V
    dist_arr[start-1] = 0
    pq = [(0, start-1)]
    while pq:
        distance, now = heapq.heappop(pq)
        if distance < dist_arr[now]:
            continue

        for next, weight in graph[now]:
            cost = distance + weight
            if cost < dist_arr[next]:
                dist_arr[next] = cost
                heapq.heappush(pq, (cost, next))

    return dist_arr

result = dijkstra(start)
for i in result:
    print("INF" if i == INF else i)
# dijik = [[INF for _ in range(V)] for _ in range(V)]
# for i in range(V):
#     dijik[i][i] = 0
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     if dijik[u-1][v-1] != INF:
#         dijik[u-1][v-1] = min(dijik[u-1][v-1], w)
#     else:
#         dijik[u-1][v-1] = w
#
# def solve(s):
#     visited = [False]*V
#     distance = [INF] * V
#     distance[s-1] = 0
#     for _ in range(V):
#         min_distance = INF
#         now=-1
#         for i in range(V):
#             if not visited[i] and distance[i] < min_distance:
#                 min_distance = distance[i]
#                 now = i
#         if now == -1:
#             break
#
#         visited[now] = True
#
#         for j in range(V):
#             if dijik[now][j] != INF and distance[now] + dijik[now][j] < distance[j]:
#                 distance[j] = distance[now] + dijik[now][j]
#
#     return distance
#
# result = solve(start)
# for i in result:
#     print('INF' if i == INF else i)