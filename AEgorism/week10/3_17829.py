N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def cnn(tbt):
    answers = []
    for i in range(2):
        for j in range(2):
            answers.append(tbt[i][j])
    answers.sort()
    return answers[2]

while N > 1:
    N //= 2
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = cnn([[arr[2*i][2*j], arr[2*i][2*j+1]],[arr[2*i+1][2*j], arr[2*i+1][2*j+1]]])
    arr = new_arr

print(arr[0][0])