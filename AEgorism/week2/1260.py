"""
DFS BFS가 뭔지는 안다. 근데 구현하는 방법을 몰라서 조금 찾아봤다.
"""
from collections import deque

graph = {}
N, M, V = map(int, input().split())
# 그래프 정의, dfs bfs할 때는 딕셔너리로 그래프를 구현한다.
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    graph[n1].sort()
    if n2 not in graph:
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)
    graph[n2].sort()

def bfs(graph, start):
    answer = []
    queue = deque([start]) # bfs에서는 큐 방식을 사용, 들어온 순서대로 나가기 때문에
    while queue:
        node = queue.popleft()
        if node not in answer:
            answer.append(node)
            if node in graph:
                temp = list(set(graph[node])-set(answer))
                temp.sort()
                queue+=temp
    return answer

def dfs(graph, start):
    answer = []
    stack = [start] # dfs에서는 스택을 사용, 탐색하는 노드에 해당하는 자식 노드를 먼저 순회해야 하기 때문
    while stack:
        node = stack.pop()
        if node not in answer:
            answer.append(node)
            if node in graph:
                temp = list(set(graph[node])-set(answer))
                temp.sort(reverse=True)
                stack+=temp
    return answer

print(*dfs(graph, V))
print(*bfs(graph, V))