n,m = map(int, input().split())

sets = {}
"""
처음에는 딕셔너리에 우겨넣으려고 했는데 시간초과가 뜨더라...
찾아보니 저번 스터디때 아놀디가 말했던 경로압축을 사용하면 될 것 같다.
"""

parents = [i for i in range(n+1)]
def find_root(x):
    if parents[x] != x:
        parents[x] = find_root(parents[x])
    return parents[x]

def union(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a != root_b:
        parents[root_b] = root_a

def is_same(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a != root_b:
        print("NO")
    else:
        print("YES")

for _ in range(m):
    ops, a, b = map(int, input().split())
    if ops == 1:
        is_same(a, b)
    else:
        union(a, b)

# def union(a, b):
#     if a not in sets:
#         sets[a] = [a]
#     if b not in sets:
#         sets[b] = [b]
#
#     combined = list(set(sets[a]) | set(sets[b]))
#     for x in combined:
#         sets[x] = combined
#
# def is_contained(a, b):
#     if a not in sets or b not in sets:
#         print("NO")
#     elif sets[a] == sets[b]:
#         print("YES")
#     else:
#         print("NO")
#
# for _ in range(m):
#     ops, a, b = map(int, input().split())
#     if ops == 1:
#         is_contained(a, b)
#     else:
#         union(a, b)