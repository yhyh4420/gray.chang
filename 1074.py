"""
1. 무조건 재귀적인 호출이다.
2. 구해야 하는 경우의 수는 2**30, 브루트포스는 에바다
3. 4개 모여있는 블럭의 첫 번호만 찾으면 된다. 거기서 +1~+3이니까. / 즉 인덱스가 [짝수][짝수]인 값만 구하면 된다.
4. N에 따라서 첫 좌표에서 더해지는 값은 2**2(N-1)이네
"""

N,r,c = map(int,input().split())

def mapping(N):
    row = [0,1]
    col = [0,2]
    if N == 1:
        return row, col
    a = 2**(2*(N-1))
    temp = mapping(N-1)
    row = temp[0] + [i+a for i in temp[0]]
    col = temp[1] + [i+(a*2) for i in temp[1]]
    return row, col

print(mapping(N)[1][r] + mapping(N)[0][c])