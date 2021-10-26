"""
섭취가능한 물고기가 없으면 현재까지의 ans를 반환한다.
    아기상어 크기 미만의 물고기만 섭취할 수 있다.
    물고기를 섭취하면 해당 칸은 빈칸이 되고 아기상어 섭취량에 + 1한다.
    섭취량이 아기상어 크기와 같아지면 섭취량은 0으로 초기화되고 아기상어 크기는 + 1 된다.

가장 가까운, 가장 위의, 가장 왼쪽의 물고기를 섭취한다. 최우선 순위 물고기를 섭취하기 위해
('거리', 'y좌표', 'x좌표') 형태로 min heap에 쌓아보고자 한다.
섭취하기 위해 이동한 시간을 ans에 더해준다.

아기상어 크기 이하의 물고기가 있는 칸들만 통과할 수있다.
"""
from collections import deque
import heapq
import sys
f_input = sys.stdin.readline

ans = 0
N = int(f_input())
pool_info = [[0] * N for _ in range(N)]
bs_pos = tuple()    #baby shark position
for i in range(N):
    for j, v in enumerate(map(int, f_input().split())):
        if v == 9:
            bs_pos = (i, j)
        pool_info[i][j] = v

# 아기상어의 초기 크기는 2이다.
bs_size = 2

# 먹은양 eat amount는 0으로 초기
e_amt = 0

while True:
    # 먹을 수 있는 물고기들을 넣을 heap
    eatable = list()

    # 방문 여부와 거리를 기록한 리스트 visited and distance 초기화
    v_n_d = [[-1] * N for _ in range(N)]
    # 최초 아기상어 위치를 queue에 넣고 bfs 시작
    queue = deque()
    queue.append(bs_pos)
    # 현재 위치 방문처리 시작위치를 0으로 잡고 한칸씩 떨어질 때마다 +1씩 해간다.
    v_n_d[bs_pos[0]][bs_pos[1]] = 0

    # 먹을 수 있는 물고기를 찾는다.
    #   1. 아기상어보다 크면 통과하지 못한다.
    #   2. 아기상어보다 작으면 통과한다. 통과하면서 거리 기록한다.
    #      거리 기록할 떄 아기상어보다 작은 물고기에 도달하는 경우 min heap에 물고기들을 넣는다.
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while queue:
        ci, cj = queue.popleft()
        for d in range(4):
            ni = ci + dy[d]
            nj = cj + dx[d]
            if 0 <= ni < N and 0 <= nj < N:
                if v_n_d[ni][nj] == -1 and pool_info[ni][nj] <= bs_size:
                    dist = v_n_d[ci][cj] + 1
                    v_n_d[ni][nj] = dist
                    queue.append((ni, nj))
                    # 만약 다음에 진행할 셀이  아기상어 미만의 크기의 크기라면 eatable heap에 넣어준다.
                    if pool_info[ni][nj] < bs_size and pool_info[ni][nj] != 0:
                        heapq.heappush(eatable, (dist, ni, nj))

    # BFS가 완료된 시점에 eatable에 하나의 물고기도 없으면 종료
    if not eatable:
        break
    else:
        e_amt += 1
        if e_amt >= bs_size:
            e_amt = 0
            bs_size += 1
        pool_info[bs_pos[0]][bs_pos[1]] = 0
        bs_pos = (eatable[0][1], eatable[0][2])
        pool_info[bs_pos[0]][bs_pos[1]] = 9
        ans += eatable[0][0]

print(ans)

