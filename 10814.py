"""
처음 주어지는 순서가 가입 순서니까 이 인덱스를 기억하면서 나이, 이름을 기억해야 하니 리스트 안에 리스트 형식으로 만들면 되겠다.
"""

N = int(input())
idx = 0
member_list = []
for _ in range(N):
    member = list(input().split())
    member.append(idx)
    member[0] = int(member[0])
    member[1], member[2] = member[2], member[1]
    member_list.append(member)
    idx += 1

member_list.sort()
for member in member_list:
    print(f"{member[0]} {member[2]}")