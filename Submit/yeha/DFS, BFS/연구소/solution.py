n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
temp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def safe():
    safe = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

def dfs(wall):
    global result
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, safe())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall += 1
                dfs(wall)
                data[i][j] = 0
                wall -= 1

dfs(0)
print(result)