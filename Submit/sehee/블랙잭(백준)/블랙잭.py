from itertools import combinations
N, M = map(int, input().split())
card = list(map(int, input().split()))


cands = list(combinations(card, 3))

answer = []
for cand in cands:
    if sum(cand) <= M:
        answer.append(sum(cand))
print(max(answer))

