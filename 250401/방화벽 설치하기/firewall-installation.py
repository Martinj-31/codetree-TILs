import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blank = []
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            blank.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def fire(board):
    q = deque([])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append([nx, ny])


def check(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt


def firewall(arr):
    global result
    if len(arr) == 3:
        a = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a[i][j] = area[i][j]
                if (i, j) in arr:
                    a[i][j] = 1
        fire(a)
        result = max(check(a), result)
        return

    for (i, j) in blank:
        if (i, j) not in arr:
            arr.append((i, j))
            firewall(arr)
            arr.pop()


result = 0
firewall([])
print(result)
