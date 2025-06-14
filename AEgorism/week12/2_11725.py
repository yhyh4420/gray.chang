"""
처음에는 부모 노드 찾는거 보고 union-find 하려고 했는데 조상 노드가 아니라 부모 노드..
그래프를 순회하면서 parent 리스트를 입력하는걸로..?
"""

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, parent):
    parents[start] = parent
    for child in graph[start]:
        if parents[child] == 0:
            dfs(child, start)

dfs(1, 0)
for i in parents[2:]:
    print(i)