from itertools import permutations

N = int(input())
list1 = list(map(int, input().split()))

cands = list(permutations(list1, len(list1)))

answer = []
for cand in cands:
    cnt = 0
    for c in range(len(cand)-1):
        cnt += abs(cand[c] - cand[c-1])
    answer.append(cnt)
print(max(answer))