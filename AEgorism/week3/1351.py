"""
재귀인거같고, 이분탐색인거 같아서 일단 이렇게 풀었을 때 음..시간초과군 왜지
찾아보니까 메모이제이션? 을 사용해야 한다고 한다.
쉽게 말해 재귀의 경우 같은 연산을 여러번 호출해야 하니까 거기에 대한 미리 저장하는 것을 의미한다
"""
dp = {}
def inf_arr(n,p,q):
    if n == 0:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = inf_arr(n//p,p,q) + inf_arr(n//q,p,q)
    return dp[n]

N, P, Q = map(int, input().split())
print(inf_arr(N,P,Q))