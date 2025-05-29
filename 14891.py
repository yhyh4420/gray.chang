import sys
from collections import deque

input = sys.stdin.readline

cycles = []
for _ in range(4):
    cycles.append(deque(list(map(int, input().split()))))

def calculate(i, spin):
    