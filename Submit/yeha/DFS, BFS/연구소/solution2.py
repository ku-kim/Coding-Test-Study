# Dave님이 공유해주신 풀이


from collections import deque
import sys

f_input = sys.stdin.readline


def spread_n_count(map_info, extN, extM):
    def count_safe(s_map):
        count = extN * extM
        for row in s_map:
            count = count - row.count(1) - row.count(2)
        return count

    c_map_info = [x[:] for x in map_info]

    queue = deque()

    visited = [[0] * extM for _ in range(extN)]

    for i in range(1, extN - 1):
        for j in range(1, extM - 1):
            if c_map_info[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

            dy = [-1, 0, 1, 0]
            dx = [0, 1, 0, -1]

            while queue:
                ci, cj = queue.popleft()

                for d in range(4):
                    ni = ci + dy[d]
                    nj = cj + dx[d]
                    if c_map_info[ni][nj] not in (1, 2) and visited[ni][nj] == 0:
                        c_map_info[ni][nj] = 2
                        queue.append((ni, nj))
                        visited[ni][nj] = 1

    return count_safe(c_map_info)


def set_wall(map_info, extN, extM, num=1):
    def check_8neighbor(inp_map, n, m):  # 8 neighbor
        score = 0
        # 현재 위치를 기준으로 상화좌우대각 총 8방향에 대해 벽이 있는지 확인.
        # 벽이 있다면 score + 1
        # 벽이 이어지지 않는다면 벽을 설치해도 바이러스를 막을 수 없으므로
        # 주변에 벽이 있는지 확인하여 이어서 벽을 설치하도록 한다.
        for a in range(n - 1, n + 2):
            for b in range(m - 1, m + 2):
                if inp_map[a][b] == 1:
                    score += 1
        if score >= 1:
            return True
        else:
            return False

    crnt_map = [x[:] for x in map_info]  # deep copy

    maximum = 0
    count = 0
    # set candidate
    candidate = list()
    for n in range(1, extN - 1):
        for m in range(1, extM - 1):
            if crnt_map[n][m] == 0 and check_8neighbor(crnt_map, n, m):
                candidate.append((n, m))

    for w in candidate:
        crnt_map[w[0]][w[1]] = 1  # set wall
        if num == 1:
            count = set_wall(crnt_map, extN, extM, num + 1)
            crnt_map[w[0]][w[1]] = 3  # 지나갔던 곳
        if num == 2:
            count = set_wall(crnt_map, extN, extM, num + 1)
            crnt_map[w[0]][w[1]] = 4  # 지나갔던 곳
        if num == 3:
            # spread the plague And measure the area of safe zone
            count = spread_n_count(crnt_map, extN, extM)
            crnt_map[w[0]][w[1]] = 5  # 지나갔던 곳
            if maximum < count:
                maximum = count
            continue

        if maximum < count:
            maximum = count

    return maximum


def isolate(map_info, N, M):
    # padding
    inp_map = [[1 for _ in range(M)]] + map_info + [[1 for _ in range(M)]]
    for i, m in enumerate(inp_map):
        inp_map[i] = [1] + m + [1]

    res = set_wall(inp_map, N + 2, M + 2)

    return res


N, M = map(int, f_input().split())
map_info = list()
for i in range(N):
    map_info.append(list(map(int, f_input().split())))

result = isolate(map_info, N, M)
print(result)
