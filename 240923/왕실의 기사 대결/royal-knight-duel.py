L, N, Q = map(int, input().split())

flat = [list(map(int, input().split())) for _ in range(L)]
knights = [list(map(int, input().split())) for _ in range(N)]
knights_hp = [0] * (N + 1)
knights_flat = [[0] * L for _ in range(L)]
knights_check = [False] * (N + 1)
for i in range(N):
    r, c, h, w, k = knights[i]
    knights_flat[r - 1][c - 1] = i + 1
    for j in range(h):
        knights_flat[r - 1 + j][c - 1] = i + 1
    for j in range(w):
        knights_flat[r - 1][c - 1 + j] = i + 1
    knights_hp[i + 1] = k

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check_grid(grid):
    for i in range(L):
        print(grid[i])


def order(i, d):
    knights_list = []
    for m in range(L):
        for n in range(L):
            if knights_flat[m][n] == i:
                if 0 <= m + dx[d] < L and 0 <= n + dy[d] < L:
                    if knights_flat[m + dx[d]][n + dy[d]] > 0 and knights_flat[m + dx[d]][n + dy[d]] != i and knights_check[knights_flat[m + dx[d]][n + dy[d]]] == False:
                        knights_check[knights_flat[m + dx[d]][n + dy[d]]] = True
                        knights_list.append(knights_flat[m + dx[d]][n + dy[d]])
    for m in knights_list:
        for j in range(L):
            for k in range(L):
                if knights_flat[j][k] == m:
                    if flat[j + dx[d]][k + dy[d]] == 2:
                        return knights_hp
                    elif flat[j + dx[d]][k + dy[d]] == 0 or flat[j + dx[d]][k + dy[d]] == 1:
                        if flat[j + dx[d]][k + dy[d]] == 1:
                            knights_hp[m] -= 1

    return knights_hp


ref = knights_hp.copy()
for _ in range(Q):
    i, d = map(int, input().split())
    knights_hp = order(i, d)
    knights_check = [False] * (N + 1)

total = 0
for i in range(len(knights_hp)):
    if knights_hp[i] == 0:
        continue
    total += (ref[i] - knights_hp[i])
print(total)