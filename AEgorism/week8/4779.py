def solve(arr):
    l = len(arr)
    if l == 1:
        return arr
    return solve(arr[:l//3]) + (l//3)*" " + solve(arr[l//3 * 2:])

while True:
    try:
        N = int(input())
        arr = "-" * (3**N)
        print(solve(arr))
    except EOFError:
        break