from collections import deque

n, m = map(int, input().split())
basecamp = [list(map(int, input().split())) for _ in range(n)]
store = [[0] * n for _ in range(n)]
ban_road = [[0] * n for _ in range(n)]
pas = [[0] * n for _ in range(n)]
store_list = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    x, y = store_list[i][0], store_list[i][1]
    for j in range(n):
        for k in range(n):
            if x - 1 == j and y - 1 == k:
                store[j][k] = i + 1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def check_grid(array):
    for i in range(n):
        print(array[i])
    print("")


def find_basecamp(id, x, y):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    x, y = x - 1, y - 1
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx, ny))
                if basecamp[nx][ny] == 1 and ban_road[nx][ny] == 0:
                    pas[nx][ny] = id
                    return


def move(id):
    x, y = -1, -1
    pas_x, pas_y = -1, -1
    for i in range(n):
        for j in range(n):
            if store[i][j] == id:
                x, y = i, j
            if pas[i][j] == id:
                pas_x, pas_y = i, j

    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx, ny))

    for i in range(4):
        nx = pas_x + dx[i]
        ny = pas_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] < visited[pas_x][pas_y]:
            pas[nx][ny] = id
            pas[pas_x][pas_y] = 0


time = 0
pas_list = []
while True:
    if time < m:
        find_basecamp(time + 1, store_list[time][0], store_list[time][1])

    for i in pas_list:
        move(i)

    if time < m:
        pas_list.append(time + 1)
        for i in range(n):
            for j in range(n):
                if pas[i][j] == time + 1:
                    ban_road[i][j] = 1

    time += 1
    if store == pas:
        break


print(time)