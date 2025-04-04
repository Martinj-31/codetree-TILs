import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
nut = [[5 for _ in range(n)] for _ in range(n)]
add_nut = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
virus.sort(key=lambda x: x[2])
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def eat():
    for v in range(len(virus)):
        if virus[v][2] == -1:
            continue
        if nut[virus[v][0] - 1][virus[v][1] - 1] >= virus[v][2]:
            nut[virus[v][0] - 1][virus[v][1] - 1] -= virus[v][2]
            virus[v][2] += 1
        else:
            virus[v][0], virus[v][1] = virus[v][0] + 10, virus[v][1] + 10


def virus_to_nut():
    for v in range(len(virus)):
        if virus[v][0] > 10 and virus[v][1] > 10:
            nut[virus[v][0] - 11][virus[v][1] - 11] += virus[v][2] // 2
            virus[v] = [-1, -1, -1]


def growth():
    for v in range(len(virus)):
        if virus[v][2] % 5 == 0:
            for d in range(8):
                nx, ny = virus[v][0] + dx[d], virus[v][1] + dy[d]
                if nx > n or nx <= 0 or ny > n or ny <= 0:
                    continue
                virus.append([nx, ny, 1])


def feed_nut():
    for i in range(n):
        for j in range(n):
            nut[i][j] += add_nut[i][j]


def check():
    cnt = 0
    for v in range(len(virus)):
        if virus[v][2] > 0:
            cnt += 1
    return cnt


for t in range(k):
    eat()
    virus_to_nut()
    growth()
    feed_nut()
print(check())
