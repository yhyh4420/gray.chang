big_map = [list(map(int, input().split())) for i in range(10)]

papers = [0,5,5,5,5,5]

def available_paper(x,y,size): # 특정 size가 들어가는지 안들어가는지 판단하는 불린 합수
    if x+size > 10 or y+size > 10:
        return False
    
    for i in range(size):
        for j in range(size):
            if big_map[x+i][y+j] == 0:
                return False
    return True

def mark(x,y,size,value):
    for i in range(size):
        for j in range(size):
            big_map[x+i][y+j] = value
    if value == 0:
        papers[size] -= 1
    else:
        papers[size] += 1


MIN = 26
def backtracking():
    global MIN
    if 25 - sum(papers) >= MIN:
        return
    
    for i in range(10):
        for j in range(10):
            if big_map[i][j] == 1:
                for size in range(5,0,-1):
                    if available_paper(i,j,size) and papers[size] > 0:
                        mark(i,j,size,0)
                        backtracking()
                        mark(i,j,size,1)
                return
    MIN = min(25-sum(papers), MIN)

backtracking()

if MIN == 26:
    print(-1)
else:
    print(MIN)