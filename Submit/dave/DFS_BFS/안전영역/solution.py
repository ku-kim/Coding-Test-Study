from collections import deque
import sys
f_input = sys.stdin.readline

N = int(f_input())
map_info = list()
min_height = 100
max_height = 1
for _ in range(N):
    row = list(map(int, f_input().split()))
    map_info.append(row)
    for r in row:
        if max_height < r:
            max_height = r
        if min_height > r:
            min_height = r

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

max_s_zone = 0
s_zone = 0
for wl in range(min_height - 1, max_height):
    # wl(water level) 보다 높은 수위의 영역이 BFS 탐색 대상이 된다.
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    s_zone = 0
    for r in range(N):
        for c in range(N):
            if map_info[r][c] > wl and visited[r][c] == 0:
                s_zone += 1
                queue.append((r, c))
                visited[r][c] = 1
                while queue:
                    cr, cc = queue.popleft()
                    for d in range(4):
                        nr = cr + dy[d]
                        nc = cc + dx[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if map_info[nr][nc] > wl and visited[nr][nc] == 0:
                                queue.append((nr, nc))
                                visited[nr][nc] = 1
            if s_zone > max_s_zone:
                max_s_zone = s_zone

print(max_s_zone)

