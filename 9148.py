def w(a, b, c, memo):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, memo)
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    if a < b < c:
        memo[(a, b, c)] = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
    else:
        memo[(a, b, c)] = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
    return memo[(a, b, c)]

memo = {}
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c, memo)}')