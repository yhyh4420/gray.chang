from collections import deque

N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr_sorted = tuple(sorted(arr))

def child(list, n, k):
    child_lists = []
    for i in range(n-k+1):
        first_child = list[:i]
        second_child = list[i:i+k][::-1]
        third_child = list[i+k:]
        child_list = first_child + second_child + third_child
        child_lists.append(tuple(child_list))
    return child_lists

def bfs(array, n, k):
    q = deque()
    visited = set()
    q.append((tuple(array), 0))
    while q:
        node, dist = q.popleft()
        visited.add(node)
        if node == arr_sorted:
            return dist
        child_list = child(node, n, k)
        for children in child_list:
            if children not in visited:
                visited.add(children)
                q.append((children, dist+1))

    return -1

print(bfs(arr, N, K))