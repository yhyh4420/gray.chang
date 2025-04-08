heights = []
for _ in range(9):
    heights.append(int(input()))
heights.sort()
not_sw = sum(heights)-100
found = False
for i in range(8):
    for j in range(i+1, 9):
        if heights[i] + heights[j] == not_sw:
            i_short = heights[i]
            j_short = heights[j]
            heights.remove(i_short)
            heights.remove(j_short)
            found = True
        if found:
            break
    if found:
        break

for h in heights:
    print(h)