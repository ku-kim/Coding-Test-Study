import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
map_info = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j, m in enumerate(map(int, sys.stdin.readline().rstrip().split()), 1):
        map_info[i][j] = m
all_cj_pos = set()  # All of chicken joint positions, 모든 치킨집 위치를 담을 집합자료구조
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if map_info[r][c] == 2:
            all_cj_pos.add((r, c))
cj_comb = combinations(all_cj_pos, M)  # 치킨집 조합 목록

a_c_dists = []  # 치킨집 조합 별로 각 집으로 부터의 치킨거리를 누적한 값들을 저장해 놓을 리스트
for cjs in cj_comb: # chicken joints 치킨집들
    acc_c_dist = 0  # 조합별 치킨거리 누적합
    # 맵 전체를 순회하면서
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            # 집을 찾을 때마다 치킨거리를 계산하여 acc_ck_dist에 더해 준다.
            if map_info[r][c] == 1:
                all_dist = []   # 집별로 치킨거리를 계산하기 위해 모든 치킨 집과의 거리를 넣을 리스트
                for cj in cjs:
                    # 집과 모든 치킨집의 거리를 계산해서 각 값을 all_dist에 넣어준다.
                    all_dist.append(abs(r - cj[0]) + abs(c - cj[1]))

                # all_dist에서 가장 작은 값이 (r, c)에서의 치킨거리가 된다.
                # 치킨거리를 조합별 치킨거리 누적합 변수에 더해준다.
                acc_c_dist += min(all_dist)
    # 이제 acc_c_dist에는 현재 조합요소에 해당하는 각 집마다의 치킨거리 총합이 들어가 있다.
    # 조합별 총 치킨거리를 a_c_dists에 넣어준다.
    a_c_dists.append(acc_c_dist)

# a_c_dists에서 가장 작은 값이 치킨거리가 가장 짧은 경우가 된다.
print(min(a_c_dists))

