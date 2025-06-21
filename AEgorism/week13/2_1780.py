import sys

input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

answer = {-1: 0, 0: 0, 1: 0}

def is_same(matrix_for_valaidate):
    base = matrix_for_valaidate[0][0]
    for i in matrix_for_valaidate:
        for j in i:
            if j != base:
                return False
    return True

def count(matrix):
    global answer
    if is_same(matrix):
        answer[matrix[0][0]] += 1
        return
    n = len(matrix)
    for i in range(0, n, n//3):
        for j in range(0, n, n//3):
            cut_matrix = [row[j:j+n//3] for row in matrix[i:i+n//3]]
            count(cut_matrix)

count(paper)
for k, v in answer.items():
    print(v)