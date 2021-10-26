"""
하나의 땅덩어리에 대해 BFS를 돌면서 바다와 인접한 셀의 좌표를 집합에 저장한다.
집합의 요소를 하나씩 꺼내서 BFS 시작점으로 삼고 BFS를 수행한다.
    - 0 인 요소들을 탐색한다.
    - 시작점과 다른 번호의 땅덩어리를 만나면 종료한다.
탐색하다가 다른 땅과 인접하면 현재 탐색한 곧까지의 거리를 확인하여 다리 길이를 최소값으로 업데이트 한다.
모든 집합 요소에 대해 위의 로직을 실행한 뒤에 다리 길이를 반환한다.
"""
from copy import deepcopy
from collections import deque
import sys
f_input = sys.stdin.readline

N = int(f_input())
map_info = [list(map(int, f_input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
l_num = 1
adjacency = set()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for r in range(N):
    for c in range(N):
        queue = deque()
        if map_info[r][c] == 1 and visited[r][c] == 0:
            queue.append((r, c))
            visited[r][c] = l_num

            while queue:
                cr, cc = queue.popleft()
                for i in range(4):
                    nr = cr + dy[i]
                    nc = cc + dx[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if map_info[nr][nc] == 1 and visited[nr][nc] == 0:
                            queue.append((nr, nc))
                            visited[nr][nc] = l_num
                        if map_info[nr][nc] == 0:
                            adjacency.add((cr, cc, l_num))
            l_num += 1

min_len = int(1e9)
for ac in adjacency:
    sr, sc, ln = ac
    b_path = [[-1] * N for _ in range(N)]
    is_conn = False
    queue = deque()
    queue.append((sr, sc))
    b_path[sr][sc] = 0
    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr = cr + dy[d]
            nc = cc + dx[d]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] != ln and visited[nr][nc] != 0:
                    is_conn = True
                    break
                if visited[nr][nc] == 0 and b_path[nr][nc] == -1:
                    queue.append((nr, nc))
                    b_path[nr][nc] = b_path[cr][cc] + 1

        if is_conn:
            break
    if min_len > b_path[cr][cc]:
        min_len = b_path[cr][cc]

print(min_len)
