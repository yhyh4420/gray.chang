## 이렇게 풀 수도 있긴 한데 정석으로 풀어보자. DFS 사용
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         a,b = map(int, input().split())
#     print(N-1)

T = int(input())

def dfs(node):
    visited[node] = True
    count = 1
    for i in range(1,N+1):
        if graph[node][i] == 1 and not visited[i]:
            count += dfs(i)
    return count

for _ in range(T):
    N ,M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    print(dfs(1)-1)
