from collections import deque

N = int(input())
operation = deque(list(input()))
alphabet = []
for _ in range(N):
    alphabet.append(int(input()))
stack = []
while operation:
    atom = operation.popleft()
    if atom.isalpha():
        stack.append(alphabet[ord(atom)-65])
    else:
        if not isinstance(stack[-2:][0], str) and not isinstance(stack[-2:][1], str):
            second = stack.pop()
            first = stack.pop()
            if atom == "+":
                result = first + second
            elif atom == "-":
                result = first - second
            elif atom == "*":
                result = first * second
            elif atom == "/":
                result = first / second
            stack.append(result)

print('%.2f' %stack[0])