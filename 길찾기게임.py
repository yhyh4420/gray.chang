import sys
sys.setrecursionlimit = (10**7)

def insert(tree, node, parent_idx):
    idx, x, y = node
    (px, py), left, right = tree[parent_idx]
    
    if px < x:
        if right != 0:
            insert(tree, node, right)
        else:
            tree[parent_idx][2] = idx
            tree[idx] = [(x,y),0,0]
    else:
        if left != 0:
            insert(tree, node, left)
        else:
            tree[parent_idx][1] = idx
            tree[idx] = [(x,y),0,0]

def solution(nodeinfo):
    new_nodeinfo = []
    for idx, [x,y] in enumerate(nodeinfo, 1):
        new_nodeinfo.append([idx, x, y])
    new_nodeinfo.sort(key = lambda x:-x[2])
    print(new_nodeinfo)
    tree = {}
    for i in range(len(nodeinfo)):
        if 
    answer = [[]]
    return answer