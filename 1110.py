N = int(input())
answer = N

def calc(N):
    a ,b = N//10, N%10
    if a+b >= 10:
        c = a+b-10
    else:
        c = a+b
    return b*10 + c

count = 0
while True:
    count += 1
    if answer == calc(N):
        break
    else:
        N = calc(N)
print(count)