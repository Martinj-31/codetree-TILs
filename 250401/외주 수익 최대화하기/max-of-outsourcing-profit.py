import sys

n = int(sys.stdin.readline())
work = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
worked = [0 for _ in range(len(work))]


def dfs(t, p):
    global result
    if t > n:
        result = max(result, p)
        return

    dfs(t + work[t - 1][0], p + work[t - 1][1])


result = 0
for i in range(1, len(work) + 1):
    dfs(i + work[i - 1][0], work[i - 1][1])
print(result)
