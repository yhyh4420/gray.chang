"""
재귀를 잘 이용합시다.
트리는 기본적으로 딕셔너리 형태를 이용하는게 좋다.
"""

N = int(input())
trees = {}
for _ in range(N):
    root, left, right = input().split(" ")
    trees[root] = [left, right]

def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(trees[root][0])
        preorder(trees[root][1])

def inorder(root):
    if root != ".":
        inorder(trees[root][0])
        print(root, end="")
        inorder(trees[root][1])

def postorder(root):
    if root != ".":
        postorder(trees[root][0])
        postorder(trees[root][1])
        print(root, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
