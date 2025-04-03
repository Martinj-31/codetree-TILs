import sys

n, m, h = map(int, sys.stdin.readline().split())
loss = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
op_loss = []
for i in range(len(loss)):
    op_loss.append([loss[i][0], loss[i][1] + 1])


def check(arr, op_arr):
    isSafe = True
    for i in range(1, n + 1):
        idx = i
        for j in range(1, h + 1):
            if [j, idx] in loss or [j, idx] in arr:
                idx += 1
            elif [j, idx] in op_loss or [j, idx] in op_arr:
                idx -= 1
        if idx != i:
            isSafe = False
            break
    return isSafe


def cand_loss():
    arr = []
    for i in range(1, n):
        for j in range(1, h + 1):
            if [j, i] in loss or [j, i + 1] in op_loss or [j, i] in op_loss or [j, i + 1] in loss:
                continue
            arr.append([j, i])
    return arr


def dfs(L, arr, idx):
    global loss_list, result
    if L == len(arr):
        op_arr = []
        for i in range(len(arr)):
            op_arr.append([arr[i][0], arr[i][1] + 1])
        if check(arr, op_arr):
            result = len(arr)
        else:
            result = -1
        return

    for i in range(idx, len(loss_list)):
        arr.append(loss_list[i])
        dfs(L, arr, i + 1)
        if result > 0:
            break
        arr.pop()


loss_list = cand_loss()
result = 0
for c in range(1, len(loss_list)):
    if c > 3:
        print(-1)
        break
    else:
        dfs(c, [], 0)
        if result > 0:
            print(result)
            break

