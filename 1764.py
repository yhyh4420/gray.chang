import sys

input = sys.stdin.readline
N,M = map(int,input().split())

duddo = []
bodo = []
for _ in range(N):
    duddo.append(input().strip())
for _ in range(M):
    bodo.append(input().strip())

answer = set(duddo) - (set(duddo) - set(bodo))
answer = list(answer)
answer.sort()
print(len(answer))
for a in answer:
    print(a)