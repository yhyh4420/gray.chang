"""
구현문제인데.. 고여있는 빗물을 구현하기 위해서는 구획화를 해야 할 것 같다.
결국에는 양동이가 몇개 있냐는 문제로 변형할 수 있는데, 그 양동이의 높이를 구해야 한다.
"""
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(1, W-1):
    left_wall, right_wall = max(blocks[:i]), max(blocks[i+1:])
    min_height = min(left_wall, right_wall)
    if blocks[i] < min_height:
        answer += (min_height - blocks[i])

print(answer)
