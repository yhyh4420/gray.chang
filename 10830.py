""""
N by N 행렬의 B제곱의 원소들을 구하는 문제이다.
"""

N,B = map(int,input().split())
M = [[*map(int, input().split())] for _ in range(N)]

def multiple(a, b):
    answer = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            sum = 0
            for i in range(N):
                sum += a[row][i] * b[i][col]
            answer[row][col] = sum % 1000

    return answer

def solve(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    temp = solve(A, B//2)
    if B%2 == 0:
        return multiple(temp, temp)
    else:
        return multiple(multiple(temp, temp), A)

result = solve(M, B)
for row in result:
    print(*row)