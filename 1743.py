"""
이거 부모 노드를 찾는 union-find 하면 될듯?
"""
import sys

sys.setrecursionlimit(10 ** 6)

N,M,K = map(int,input().split())
food_position = []
food_index = {}
for i in range(K):
    x,y = map(int,input().split())
    food_position.append((x,y))
    food_index[(x,y)] = i

parent = [i for i in range(K)]
size = [1 for _ in range(K)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(K):
    x,y = food_position[i]
    for j in range(4):
        new_x = x + dx[j]
        new_y = y + dy[j]
        if (new_x, new_y) in food_position:
            union(i, food_position.index((new_x, new_y)))

print(max(size))