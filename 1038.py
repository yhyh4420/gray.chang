"""
규칙이 있는듯. 한자리수는 무조건 감소하는 수이고, 두자리수는 1이면 10, 2이면 21, 20, 3이면 32, 31, 30,....
몇자리 없을거 같은데 브루트포스로 합시다
"""
# from itertools import combinations
#
# n = int(input())
#
# num = []
# for i in range(1,11):
#     for j in list(combinations(range(10),i)):
#         number = ""
#         j = sorted(list(j), reverse=True)
#         for k in j:
#             number += str(k)
#         num.append(int(number))
# num = list(set(num))
# num.sort()
# if n >= len(num):
#     print(-1)
# else:
#     print(num[n])

"""
지금은 브루트포스로 리스트를 결정했는데, 백트래킹 방식도 있을 것 같다.
"""
n = int(input())

num = []

def backtrack(depth, length, current): # 일단 백트래킹 설정, 현재 뎁스와 목표 뎁스, 현재 상태 저장
    if depth == length: # 뎁스가 목표 뎁스에 도달하면
        num.append(int(current)) # 리스트에 저장함
        return # 끝!
    for i in range(10): #
        if not current or int(current[-1]) > i:
            backtrack(depth + 1, length, current + str(i))

for i in range(1, 11):
    backtrack(0, i, "")

num.sort()
if n >= len(num):
    print(-1)
else:
    print(num[n])