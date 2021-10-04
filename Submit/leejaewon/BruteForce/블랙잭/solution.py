import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(max([sum(val) for val in combinations(arr, 3) if sum(val) <= m]))