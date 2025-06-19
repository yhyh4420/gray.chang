"""
일단 맵부터 만들어야 할 듯

1. 자신이 좋아하는 학생이 이미 배치된지 확인한다.
2. 1번 조건을 만족한다면 순회하면서 좋아하는 학생의 번호가 가장 많이 인접한 곳을 찾는다.
3. 1번 조건을 만족하지 않는다면 순회하면서 빈칸이 가장 많은 곳에 넣는다.
"""

import sys
input = sys.stdin.readline

N = int(input())
student_like = []
for _ in range(N**2):
    student_like.append(list(map(int, input().split())))

classroom = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for students in student_like:
    student, like = students[0], students[1:]
    best = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j] != 0:
                continue
            empty_count = 0
            like_count = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if classroom[ni][nj] == 0:
                        empty_count += 1
                    elif classroom[ni][nj] in like:
                        like_count += 1
            best.append((like_count, empty_count, i, j))
    best.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    classroom[best[0][2]][best[0][3]] = student

like_score = [0, 1, 10, 100, 1000]
student_dict = {student[0]: student[1:] for student in student_like}
answer = 0
for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        like = student_dict[student]
        count = 0
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < N and 0 <= nj < N:
                if classroom[ni][nj] in like:
                    count += 1
        answer += like_score[count]
print(answer)