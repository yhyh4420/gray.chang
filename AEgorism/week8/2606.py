from collections import deque

N = int(input())
E = int(input())
graph = {}
for _ in range(E):
    a,b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

def bfs(graph):
    answer = []
    queue = deque([1])
    while queue:
        node = queue.popleft()
        if node not in answer:
            answer.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(answer))
                queue.extend(temp)
    return answer

print(len(bfs(graph))-1)