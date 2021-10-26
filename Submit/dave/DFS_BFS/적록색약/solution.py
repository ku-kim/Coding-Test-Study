from collections import deque
import sys
f_input = sys.stdin.readline
N = int(f_input())
pic = list()
for _ in range(N):
    pic.append([c for c in f_input().rstrip()])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ordinary = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            ordinary += 1
            color = pic[i][j]
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                ci, cj = queue.popleft()
                for d in range(4):
                    ni = ci + dy[d]
                    nj = cj + dx[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if pic[ni][nj] == color and visited[ni][nj] == 0:
                            queue.append((ni, nj))
                            visited[ni][nj] = 1

color_blind = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color_blind += 1
            c_tbl = {'R': 1, 'G': 1, 'B': 2}
            color = c_tbl[pic[i][j]]
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                ci, cj = queue.popleft()
                for d in range(4):
                    ni = ci + dy[d]
                    nj = cj + dx[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if c_tbl[str(pic[ni][nj])] == color and visited[ni][nj] == 0:
                            queue.append((ni, nj))
                            visited[ni][nj] = 1

print(ordinary, color_blind)

