S = input()

arr = []
for i in range(1, len(S)+1):
    for j in range(len(S)-i+1):
        arr.append(S[j:j+i])
arr_set = set(arr)
print(len(arr_set))