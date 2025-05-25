N, M = map(int,input().split())

arr = [i+1 for i in range(N)]
visited = [False] * N

# def backtrack(answer):
#     if len(answer) == M:
#         print(*answer)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             backtrack(answer + [arr[i]])
#             visited[i] = False

def backtrack(answer):
    if len(answer) == M:
        print(*answer)
        return

    for i in range(1,N+1):
        if i not in answer:
            backtrack(answer + [i])

backtrack([])