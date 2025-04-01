import sys

n = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0 for _ in range(n)]


def dfs(L, idx):
    global minimum
    if L == n // 2:
        morning = 0
        night = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    morning += table[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    night += table[i][j]
        minimum = min(minimum, abs(morning - night))
        return

    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(L + 1, i + 1)
            visited[i] = 0


minimum = 1e9
dfs(0, 0)
print(minimum)
