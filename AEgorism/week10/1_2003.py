N, M = map(int, input().split())
A = list(map(int, input().split()))
sumA = [0]
sums = 0
for i in range(N):
    sums += A[i]
    sumA.append(sums)

"""
투포인터 한번 써볼까.
"""
count = 0
start, end = 0, 1
while start <= end:
    if end == N+1:
        break
    sum_validation = sumA[end] - sumA[start]
    if sum_validation == M:
        count += 1
        start += 1
        end = start + 1
    elif sum_validation > M:
        start += 1
        end = start + 1
    else:
        end += 1

print(count)
"""
생각해보니 반복문도 괜찮을듯. N이 10,000까지인데 누적합의 경우 복잡도가 O(0.5*N**2) 이렇게 나오니까 최악의 경우에도 오천만임
아니 이것도 시간초과네 개빡치게 
"""
# count = 0
# for start in range(N):
#     for end in range(start, N):
#         sum_validation = sumA[end+1]-sumA[start]
#         if sum_validation > M:
#             continue
#         if sum_validation == M:
#             count += 1
#
# print(count)

"""
이 밑에가 시간초과란다. 왜?
"""
# count = 0
# def backtrack(start, end):
#     global count
#     if start == N or end ==N:
#         return
#     sum_validation = sumA[end+1]-sumA[start]
#     if sum_validation > M:
#         return
#     elif sum_validation == M:
#         count += 1
#         return
#
#     backtrack(start, end+1)
#     backtrack(start+1, end+1)
#
# backtrack(0,0)
# print(count)