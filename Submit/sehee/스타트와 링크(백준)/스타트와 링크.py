from itertools import combinations
N = int(input())

cand = list(combinations(range(N), N//2))

cand_list = list(list(map(int, input().split())) for _ in range(N))


answer = []
for t in range(len(cand) // 2):
    start = 0
    for i in cand[t]:
        for j in cand[t]:
            start += cand_list[i][j]

    link = 0
    for i in cand[-(t+1)]:
        for j in cand[-(t+1)]:
            link += cand_list[i][j]

    answer.append(abs(start - link))

print(min(answer))


# result = []
# while cand:
#     i, j = cand.popleft()
#     a, b = cand.pop()
#     start = cand_list[i][j] + cand_list[j][i]
#     link = cand_list[a][b] + cand_list[b][a]
#
#     result.append(abs(start - link))
#
# print(min(result))