import sys

N = int(input())
ingredients = []
for _ in range(N):
    ingredients.append(list(map(int, input().split())))

answer = sys.maxsize
def backtracking(i, picks):
    global answer
    if picks:
        S, B = 1, 0
        for pick in picks:
            S *= pick[0]
            B += pick[1]
        answer = min(answer, abs(S-B))
    if i == N:
        return

    picks.append(ingredients[i])
    backtracking(i+1, picks)
    picks.pop()
    backtracking(i+1, picks)

backtracking(0,[])
print(answer)