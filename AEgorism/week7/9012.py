def solution(arr):
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

N = int(input())

for _ in range(N):
    arr = input()
    solution(arr)