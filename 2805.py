"""
처음에는 너무 간단하게 구현하려고 했다. 근데 틀린것도 아니고, 시간초과?
이상해서 조건을 다시 봤다. 나무의 개수는 100만으로, 크게 문제될 것은 없고, 다만 문제될 것은 나무의 길이일 것 같다.(10억)
단순하게 찾으면 나무길이 최대값에서 1씩 줄여가면서 찾아야 하는데, 이러면 N의 복잡도로, 이걸 줄여야 한다.
어떻게? 제일 먼저 생각나는건 이진탐색이다. 해보자
"""
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)-1
# 시작이랑 끝을 정하고, 해당 인덱스를 동적으로 바꿔가며 탐색하는 방식

while start <= end: # start와 end를 동적으로 바꿀거기 때문에 이에 대한 조건
    mid = (start + end) // 2 # 중간값을 구하기

    cuttings = 0
    for tree in trees:
        if tree >= mid:
            cuttings += (tree-mid) # mid보다 큰 나무는 다 컷팅

    if cuttings >= M: # 원하는 양만큼 컷팅했으면 더 높은 곳에서도 컷팅 가능한지 확인
        start = mid + 1
    else: # 원하는 양만큼 컷팅 못했으면 낮은 곳에서 컷팅 실시
        end = mid - 1

print(end)

# 이전에 한거(단순탐색)
# answer = max(trees) - 1
# count = 0
#
# while True:
#     for i in range(N):
#         if trees[i] > answer:
#             cut_tree = trees[i]-answer
#             count += cut_tree
#     if count >= M:
#         break
#     else:
#         answer -= 1
#         count = 0
#
# print(answer)