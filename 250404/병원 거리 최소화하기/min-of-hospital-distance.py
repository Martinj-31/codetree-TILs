import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
hos = []
man = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            man.append([i, j])
        elif board[i][j] == 2:
            hos.append([i, j])


def dfs(cnt, arr, idx):
    global result
    if len(arr) == cnt:
        dist_list = []
        for a in range(len(arr)):
            for m in range(len(man)):
                dist_list.append(dist(man[m], arr[a]))
        dist_list.sort()
        result = min(result, sum(dist_list[:len(man)]))
        return

    for h in range(idx, len(hos)):
        arr.append(hos[h])
        dfs(cnt, arr, h + 1)
        arr.pop()


def dist(man_pos, hos_pos):
    return abs(man_pos[0] - hos_pos[0]) + abs(man_pos[1] - hos_pos[1])


result = 1e9
dfs(m, [], 0)
print(result)