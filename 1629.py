A, B, C = map(int, input().split())

"""
접근법
단순히 나머지를 구하는 것이 아니라 매우매우 큰 값을 주고 효율적으로 계산하라는 문제
예전에 푼 적이 있어서 찾아보니 이게 분할정복이더라.
근데 그때랑 다른 접근법으로 풀려고 했음(실패함)
- 과거에는 temp를 두고 재귀적으로 호출
- 이번에는 temp값을 return문에 두고 재귀적으로 호출(temp 안씀)

똑같은 코드라고 생각했는데 심각한 문제가 있었다.
문제점 : temp를 안쓰고 바로 함수를 호출하면 매 순간순간 호출해야 하기 때문에 시간복잡도가 logN에서 N으로 증가한다.
평소라면 문제 안되겠지만 분할정복은 재귀이다. 재귀에서 불필요한 호출하면 백수된다.
"""
def solve(A, B, C):
    if B == 1:
        return A%C
    temp = solve(A, B//2, C)
    if B % 2 == 1:
        return temp*temp*A%C
    else:
        return temp*temp%C

print(solve(A, B, C))

"""
추가로 파이썬 내장모듈에는 pow()라는 것이 있다.
pow(A,B,C)를 하면 자동으로 (A**B)%C를 리턴해주는데, 분할정복을 기반으로 구현되어있다.
"""

# --------- 내가 풀고 실패한거----------------
# A, B, C = map(int, input().split())
#
# def solve(A, B, C):
#     if B == 1:
#         return A%C
#     if B % 2 == 1:
#         return (solve(A, B//2, C) * solve(A, B//2, C) * A%C)%C
#     else:
#         return (solve(A, B//2, C) * solve(A, B//2, C))%C
#
# print(solve(A, B, C))