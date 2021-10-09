from itertools import combinations
N, M = map(int, input().split())
roads = list(list(map(int, input().split())) for _ in range(N))

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if roads[i][j] == 1:
            house.append((i, j))
        elif roads[i][j] == 2:
            chicken.append((i, j))

cands = list(combinations(chicken, M))

#
# result = []
# for cand in cands:
#     print("치킨집 조합", cand)
#     answer = 0
#     for h in house:
#         list1 = []
#         print("집", h)
#         for x, y in cand:
#             print("치킨집 좌표", (x, y))
#             list1.append(abs(h[0]-x) + abs(h[1]-y))
#             print("모든 치킨거리", list1)
#         answer += min(list1) # 집 하나당 치킨거리 모두 더하면
#         print("치킨집 조합 하나 당 도시의 치킨거리", answer)
#     result.append(answer)
# print(result)
# print("가장 작은 도시의 치킨거리", min(result))



result2 = []
for cand in cands:
    result = []
    for h in house:
        list1 = []
        for x, y in cand:
            list1.append(abs(h[0]-x) + abs(h[1]-y))
            print("list1", list1)
        result.append(min(list1))
    result2.append(sum(result))
print("result", min(result2))

