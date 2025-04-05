people = 0
lists = []
for _ in range(10):
    o, i = map(int, input().split())
    people += (i-o)
    lists.append(people)

print(max(lists))