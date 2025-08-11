"""
에라토스테네스 체 => 2,4,6...제거 후 3,6,9...제거
"""
## 공부할때
# chae = [True for i in range(1000001)]
# chae[0], chae[1] = False, False

# for i in range(2,1000000):
#     if chae[i]: # i*2, i*3... false로 매핑
#         for j in range(i*i, 1000001, i):
#             chae[j] = False
            
# M,N = map(int, input().split())
# for idx in range(M,N+1):
#     if chae[idx]:
#         print(idx)

# 빠른버전
M,N = map(int, input().split())
for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:  # for문이 break없이 끝났을 때
        print(i)