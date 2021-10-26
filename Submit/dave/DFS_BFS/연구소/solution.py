"""
연구소의 최대 크기는 8 x 8 = 64
세울 수 있는 벽의 개수는 3개
따라서 모든 칸이 비워진 상태에서 벽을 세울 수 있는 경우의 수는 64 C 3 = 41,664 개
벽을 제외한 나머지 노드의 수 61가 있다고 할 때 DFS의 시간복잡도는 V^2 이므로 61 * 61 = 3,721
그러므로 41,664 * 3,721 = 155,031,744 번의 연산을 진행하게 되어 조합을 사용한 풀이가 가능할 것으로 보인다.
"""
from collections import deque
from itertools import combinations as comb
import sys
f_input = sys.stdin.readline

map_info = list()
empty_pos = set()
virus_pos = list()
N, M = map(int, f_input().split())
# 연구소 정보를 입력 받으면서 비어있는 공간의 좌표를 별도로 저장한다.
# 비어 있는 좌표는 조합을 사용하여 그 중 3개를 선택해서 1로 바꾸는 작업을 진행할 예정이다.
b_cnt = 0   # block count
for i in range(N):
    row_info = list(map(int, f_input().split()))
    map_info.append(row_info)

    for j in range(M):
        if row_info[j] == 0:
            empty_pos.add((i, j))
        if row_info[j] == 1:
            b_cnt += 1
        if row_info[j] == 2:
            virus_pos.append((i, j))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

max_safety_areas = 0

for e_pos in comb(empty_pos, 3):
    visited = set()
    queue = deque(virus_pos)
    while queue:
        c_pos = queue.popleft()
        # n_pos = c_pos[0] + dy, c_pos[1] + dx
        # e_pos는 임의의 세 벽이 세워지는 공간임.
        # visited는 이미 방문한 공간임.
        # n_pos는 0 and n_pos가 e_pos나 visited에 없을 것.
        for d in range(4):
            n_pos = (c_pos[0] + dy[d], c_pos[1] + dx[d])
            if 0 <= n_pos[0] < N and 0 <= n_pos[1] < M:
                if map_info[n_pos[0]][n_pos[1]] == 0 and n_pos not in e_pos and n_pos not in visited:
                    queue.append(n_pos)
                    visited.add(n_pos)

    # N * M - 기본 벽돌 수 - 3 - visited 원소 수 - 기본 바이러스 위치 수
    safety_areas = N * M - b_cnt - 3 - len(visited) - len(virus_pos)
    if max_safety_areas < safety_areas:
        max_safety_areas = safety_areas

print(max_safety_areas)

