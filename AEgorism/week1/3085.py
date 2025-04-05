n = int(input())

m = []
for _ in range(n):
    m.append(list(input()))

answer = 1
def max_count():
    max_count = 1
    for i in range(n):
        garo_count = 1
        for j in range(n-1):
            if m[i][j] == m[i][j+1]:
                garo_count+=1
            else:
                garo_count=1
            max_count = max(max_count, garo_count)

        sero_count = 1
        for j in range(n-1):
            if m[j][i] == m[j+1][i]:
                sero_count+=1
            else:
                sero_count=1
            max_count = max(max_count, sero_count)
    return max_count

answer = 1
for i in range(n):
    for j in range(n-1):
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
        answer = max(answer, max_count())
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]
        m[j][i], m[j+1][i] = m[j+1][i], m[j][i]
        answer = max(answer, max_count())
        m[j][i], m[j + 1][i] = m[j + 1][i], m[j][i]
print(answer)

# for i in range(n):
#     for j in range(n-1):
#         garo_answer = 1 # 각 로직에 대한 최대값 임시저장 변수, 기준은 하나의 행 또는 열에 대한 비교가 완료되었을 때의 최대값이다.
#         sero_answer = 1
#         m[i][j], m[i][j+1] = m[i][j+1], m[i][j] # 가로방향으로 바꿈
#         for k in range(n-j-1):  # 가로방향을 순차적으로 비교
#             if m[i][j] == m[i][j+k+1]:
#                 garo_answer += 1
#             else: garo_answer = 1
#         for k in range(n-i-1):  # 세로방향을 순차적으로 비교
#             if m[i][j] == m[i+k+1][j]:
#                 sero_answer += 1
#             else: sero_answer = 1
#         m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]  # 바꾼거 되돌림
#         answer = max(answer, garo_answer, sero_answer)
#
#         garo_answer = 1 # 변수 초기화
#         sero_answer = 1
#         m[j][i], m[j+1][i] = m[j+1][i], m[j][i] # 세로방향으로 바꿈
#         for k in range(n-i-1):  # 가로방향을 순차적으로 비교
#             if m[j][i] == m[j][i+k+1]:
#                 garo_answer += 1
#         for k in range(n-j-1):  # 세로방향을 순차적으로 비교
#             if m[j][i] == m[j+k+1][i]:
#                 sero_answer += 1
#         m[j][i], m[j+1][i] = m[j+1][i], m[j][i]  # 바꾼거 되돌림
#         answer = max(answer, garo_answer, sero_answer)
#
#
# print(answer)