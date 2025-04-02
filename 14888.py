"""
도저히 어떻게 푸는지 모르겠다. 알고리즘을 봤는데, 백트래킹이라는 것을 쓴단다.
백트래킹은 프루닝과 비슷한 개념인데, 도저히 최적해가 아니라면 제거하는 방식이다.
"""

N = int(input())
lists = list(map(int, input().split()))
ops = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def backtrack(depth, total, plus, minus, multiple, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus:
        backtrack(depth+1, total+lists[depth], plus-1, minus, multiple, divide)
    if minus:
        backtrack(depth+1, total-lists[depth], plus, minus-1, multiple, divide)
    if multiple:
        backtrack(depth+1, total*lists[depth], plus, minus, multiple-1, divide)
    if divide:
        if total >= 0:
            total = total // lists[depth]
        else:
            total = ((-total) // lists[depth])*-1
        backtrack(depth+1, total, plus, minus, multiple, divide-1)

backtrack(1,lists[0], ops[0], ops[1], ops[2], ops[3])
print(int(maximum))
print(int(minimum))
