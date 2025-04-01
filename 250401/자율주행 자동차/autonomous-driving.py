import sys

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = [0, 1, 2, 3]


cnt = 1
road[x][y] = 2
while True:
    for _ in range(4):
        d = dir[d - 1]
        nx, ny = x + dx[d], y + dy[d]
        if road[nx][ny] == 0:
            cnt += 1
            road[nx][ny] = 2
            x, y = nx, ny
            break
    else:
        d = dir[d - 2]
        nx, ny = x + dx[d], y + dy[d]
        if road[nx][ny] == 1:
            break
        d = dir[d - 2]
        x, y = nx, ny

print(cnt)
