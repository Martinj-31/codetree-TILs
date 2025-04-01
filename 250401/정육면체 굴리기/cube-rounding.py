import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

dir_order = list(map(int, sys.stdin.readline().split()))

dEast, dWest, dSouth, dNorth, dBottom, dUp = 0, 0, 0, 0, 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for o in dir_order:
    nx, ny = x + dx[o - 1], y + dy[o - 1]
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
    if o == 1:
        dEast, dWest, dSouth, dNorth, dBottom, dUp = dUp, dBottom, dSouth, dNorth, dEast, dWest
    elif o == 2:
        dEast, dWest, dSouth, dNorth, dBottom, dUp = dBottom, dUp, dSouth, dNorth, dWest, dEast
    elif o == 3:
        dEast, dWest, dSouth, dNorth, dBottom, dUp = dEast, dWest, dBottom, dUp, dNorth, dSouth
    elif o == 4:
        dEast, dWest, dSouth, dNorth, dBottom, dUp = dEast, dWest, dUp, dBottom, dSouth, dNorth

    if board[nx][ny] == 0:
        board[nx][ny] = dBottom
    else:
        dBottom, board[nx][ny] = board[nx][ny], 0
    print(dUp)
    x, y = nx, ny

