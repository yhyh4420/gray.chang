import sys
input = sys.stdin.readline

N = int(input())
members = [list(map(int, input().split())) for _ in range(N)]
members_availability = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        members_availability[i][j] = members[i][j] + members[j][i]

visited = [False] * (N+1)

answer = sys.maxsize
def backtrack(depth, idx):
    global answer
    if depth == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    link += members_availability[i][j]
                elif not visited[i] and not visited[j]:
                    start += members_availability[i][j]
        answer = min(answer, abs(start-link))
    for k in range(idx,N):
        if not visited[k]:
            visited[k] = True
            backtrack(depth+1, k+1)
            visited[k] = False

backtrack(0, 0)
print(answer)