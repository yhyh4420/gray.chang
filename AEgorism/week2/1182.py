from itertools import combinations

N, S = map(int, input().split())
num = list(map(int, input().split()))

"""
백트래킹이 뭔가. 일단 파라미터를 처음으로 설정하고 알아서 재귀를 돌린 뒤 글로벌변수를 바꾸는 방식으로 진행된다.
일단 해보자
"""
count = 0
def sum_arr(idx, sub_sum):
    global count
    if idx == N: # 인덱스가 범위를 벗어나면 탈출
        return
    sub_sum += num[idx] # 먼저 인덱스의 값을 더함

    if sub_sum == S:
        count += 1

    sum_arr(idx+1, sub_sum) # 더한 상태로 다음으로 간다
    sum_arr(idx+1, sub_sum-num[idx])  # 더하지 않은 상태로 다음으로 간다

sum_arr(0, 0)

print(count)

"""
좋은 방법은 아니긴 한데, itertools에 combinations라는 라이브러리가 있다.
이건 브루트포스로 모든 경우의 수를 찾는 방식이다.
"""

# for i in range(1,N+1):
#     combs = combinations(num,i)
#     for comb in combs:
#         if sum(comb) == S:
#             count += 1
# print(count)