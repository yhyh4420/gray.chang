N = int(input())

container = [0]*1001
max_h = 0
max_l = 0
for _ in range(N):
    L, H = map(int, input().split())
    container[L] = H
    if H > max_h:
        max_h = H
        max_l = L

height = 0
answer = container[:]
for i in range(max_l+1):
    if container[i] > height:
        height = container[i]
    answer[i] = height

height = 0
for i in range(1000,max_l,-1):
    if container[i] > height:
        height = container[i]
    answer[i] = height

print(sum(answer))

"""
생각의 방향은 맞았으나 구현을 이상하게 해서 헷갈린 문제
굳이 이중for문을 돌지 않아도 height를 기억하기만 하면 된다.
"""