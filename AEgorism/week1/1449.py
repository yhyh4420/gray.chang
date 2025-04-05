N, L = map(int, input().split())

pipes = list(map(int, input().split()))
pipes = sorted(pipes) # 일단 풀기쉽게 sort

"""
풀기 전에 생각한거
1. 좌우 0.5라고 해서 소수를 생각하지 말자. 어차피 n의 위치에 테이프를 붙이는 최적은 n-0.5와 n+0.5를 포함하게 붙이는 거니까 정수만 생각해도 될듯.
2. 겹치는 것도 가능하다. 처음에 리스트를 받은 최적방법으로 테이프를 붙이게 된 위치를 제거하는 방식으로 while문을 돌리면 되지 않을까? 
"""

count = 0 # 붙인 테이프 개수
while len(pipes) != 0: # 다 붙이면 끝난거임
    patched = pipes[0] # 붙이지 않은 위치 중 첫번째 위치 기억
    count += 1 # 첫번째 위치에 테이프 붙임
    pipes.remove(patched) # 붙였으니 리스트에서 제거
    new_pipes = pipes[:] # for문 돌리기 위해 리스트 얕은 복사
    for i in new_pipes: # 한 테이프로 다른 위치를 커버할 수 있나 검증
        if patched + L > i: # 만약 patched에 붙인 테이프가 다음 파이프 위치를 커버한다면
            pipes.remove(i) # 제거
        else: break # 아니면 또다른 테이프 붙여야되니까 for문 종료, 다음 count 올릴 준비

print(count)

"""
틀린점
1. 로직은 처음부터 맞았음
2. 하지만 리스트 요소를 순회하면서 리스트 요소를 삭제하니까 순차적으로 확인하려는 의도에 맞지 않았음(뛰어넘고 그러던데)
3. 순차적으로 순회하고 리스트를 삭제하기 위해 for문용 리스트를 얕은 복사 해왔더니 해결(처음에는 new_pipes = pipes로 했더니 같은 주소를 참조해서 동일한 결과였음)  
"""