import sys
from itertools import combinations as comb


r_line = sys.stdin.readline
N = int(r_line().rstrip())
S = [[0] * (N + 1)]
for _ in range(N):
    S.append([0] + [ap for ap in map(int, r_line().rstrip().split())])


members = {i for i in range(1, N + 1)}  # 참여자 전원
min_diff_abt_sum = int(1e9)  # 두 팀의 능력치 합계 차가 최인 값.
# 능력치를 계산해서 {{1, 2, ...}: 능력치 총 합} 형태의 딕셔너리에 저장하고
# 이후 같은 멤버 구성에 대한 능력치 계산이 요구되면 dictionary의 값을 사용하도록 처리
abt_p_dict = dict()   # ability point dictionary
for el in comb(members, N // 2):
    start_team_abt_sum = 0  # start team 능력치 합
    link_team_abt_sum = 0   # link team 능력치 합
    start_team_members = tuple(el)    # start team 구성원
    link_team_members = tuple(members.difference(set(el)))  # link team 구성원

    # start team의 능력치 합을 구한다.
    if start_team_members not in abt_p_dict:
        # (i, j)를 combinations를 통해 생성하여 각각 접근해야 중복을 막을 수 있다.
        pair_of_members = comb(start_team_members, 2)
        for pom in pair_of_members:
            start_team_abt_sum += S[pom[0]][pom[1]] + S[pom[1]][pom[0]]
        abt_p_dict[start_team_members] = start_team_abt_sum
    else:
        start_team_abt_sum = abt_p_dict[start_team_members]

    # link team의 능력치 합을 구한다.
    if link_team_members not in abt_p_dict:
        pair_of_members = comb(link_team_members, 2)
        for pom in pair_of_members:
            link_team_abt_sum += S[pom[0]][pom[1]] + S[pom[1]][pom[0]]
        abt_p_dict[link_team_members] = link_team_abt_sum
    else:
        link_team_abt_sum = abt_p_dict[link_team_members]

    if min_diff_abt_sum > abs(start_team_abt_sum - link_team_abt_sum):
        min_diff_abt_sum = abs(start_team_abt_sum - link_team_abt_sum)

print(min_diff_abt_sum)

