"""
벨만 포드 알고리즘 써야한답니다
간선 weight가 양수면 다익스트라, 음수 있으면 벨만 포드
다익스트라는 음수가 있을 경우 최소거리를 찾을 수 없기 때문
모든 노드에 대한 모든 엣지를 순회(시작지점 제외하니까 V-1이고, E임)
만약 V번째에도 순회한다? 그러면 무한루프 있는거임.
"""
import sys

input = sys.stdin.readline

V,E = map(int, input().split())
graph = []
INF = float('inf')
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph.append((start, end, weight))

def bellman(start):
    dist = [INF] * (V+1)
    dist[start] = 0
    for i in range(V):
        for start, end, weight in graph:
            if dist[start] != INF and dist[start] + weight < dist[end]:
                if i == V-1: # 여기가 핵심. V번째에도 찾은거니까 이건 무한루프 도는거임
                    return True, []
                dist[end] = dist[start] + weight
    return False, dist

is_circluar, dist = bellman(1)
if is_circluar:
    print(-1)
else:
    for i in range(2,V+1):
        print(-1 if dist[i] == INF else dist[i])