"""
    N = 카드 개수 (3 <= N <= 100)
    M = 딜러가 제안하는 수 (10 <= M <= 300,000)

    N개의 카드 가운데 3장을 뽑아 M보다 작은 수를 만들되 그 중 가장 큰 수를 반환한다.
"""
from itertools import combinations as comb
import sys
r_line = sys.stdin.readline


N, M = map(int, r_line().rstrip().split())
cards = list(map(int, r_line().rstrip().split()))

max_val = 0
for c in comb(cards, 3):
    if max_val < sum(c) <= M:
        max_val = sum(c)

print(max_val)

