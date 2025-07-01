"""
그냥 더하기 때리면 되는 간단한 문제..
그런데 골드인건 이유가 있겠지?
그럼그렇지 그냥 브루트포스로 풀면 시간복잡도가 NxM어서 나가리다
처음에는 n번까지 번호가 매겨져있다고 생각해서 직원 번호가 중복이 안된다고 생각했다.
그래서 단순 누적합으로 풀었는데 틀림이 나왔다. 반례를 만들어달라고 GPT한테 부탁하니 같은 숫자 여러개 나오는걸 말해주네
흠 그러면 탐색인데
"""
import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
up_list = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for i in range(1, n):
    parent = up_list[i]
    tree[parent].append(i+1)

clap = [0]*(n+1)
for _ in range(m):
    i, w = map(int, input().split())
    clap[i] += w

def dfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for child in tree[node]:
            clap[child] += clap[node]
            q.append(child)

dfs()
print(*clap[1:])