import sys

n = int(sys.stdin.readline())
work = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
worked = [0 for _ in range(len(work))]


def dfs(t, p):
    global result
    if t >= n:
        result = max(result, p)
        return

    if t + work[t][0] > n:
        dfs(t + work[t][0], p)
        dfs(t + 1, p)
    else:
        dfs(t + work[t][0], p + work[t][1])


result = 0
for i in range(len(work)):
    if i + work[i][0] <= n:
        dfs(i + work[i][0], work[i][1])
print(result)


# 3
# 1 20
# 4 30
# 1 30