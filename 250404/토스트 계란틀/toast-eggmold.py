import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().split())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global eggs
    visited = [[0 for _ in range(n)] for _ in range(n)]
    shaking = False
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 1:
                continue
            q = deque([[x, y]])
            visited[x][y] = 1
            sum_eggs = eggs[x][y]
            cnt_eggs = 1
            egg_list = [[x, y]]
            while q:
                xx, yy = q.popleft()
                for d in range(4):
                    nx, ny = xx + dx[d], yy + dy[d]
                    if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny] == 1:
                        continue
                    if L <= abs(eggs[nx][ny] - eggs[xx][yy]) <= R:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        sum_eggs += eggs[nx][ny]
                        cnt_eggs += 1
                        egg_list.append([nx, ny])
                        shaking = True
            afterShaking = sum_eggs // cnt_eggs
            for i, j in egg_list:
                eggs[i][j] = afterShaking
    return shaking


cnt = 0
while True:
    result = bfs()
    if not result:
        break
    cnt += 1
print(cnt)
