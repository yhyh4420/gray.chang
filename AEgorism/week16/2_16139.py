import sys

data = sys.stdin.read().splitlines()

string = data[0].strip()
length = len(string)
q = int(data[1])

memory = {}
memory_keys = set(string)
for key in memory_keys:
    l = [0]*(length+1)
    idx = 0
    for c in string:
        idx += 1
        if c == key:
            l[idx] = l[idx-1] + 1
        else:
            l[idx] = l[idx-1]
    memory[key] = l

def solution(c, start, end):
    return memory[c][end+1]-memory[c][start]

lines = data[2:]

for line in lines:
    alphabet, s, e = line.split()
    s, e = int(s), int(e)
    print(solution(alphabet, s, e)) if alphabet in memory else print(0)