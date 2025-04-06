"""
방향 없는 그래프, 연결 요소의 개수를 구해야 한다.
연결 요소는 무엇인가? 그래프를 구성했을 때 노드로 연결되지 않는 각각의 그래프로 이해하면 좋을 것 같다.
그러면 그래프 탐색을 해서 순회하는 요소를 리스트로 저장하면 될 것 같다.
"""
import sys

# 일단 그래프부터 만들기
N, M = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = graph[n2][n1] = 1

def dfs(start):
    visited[start] = True # 시작지점이니까 방문하는거임
    for i in range(1, N+1): # 1부터 N까지
        if not visited[i] and graph[start][i] == 1: # 만약 방문하지 않았고, start와 i가 연결되어있다면?
            dfs(i) # 재귀로 탐색

count = 0
sys.setrecursionlimit(10 ** 6) # 파이썬에서 정해준 깊이를 넘어가면 에러가 발생하는데 그거 방지
for i in range(1,N+1):
    if not visited[i]: # 방문을 안했으면 그룹 수를 하나 늘리고 dfs 실시, 방문 했으면 걍 넘기고
        count += 1
        dfs(i)
print(count)