import sys
from collections import deque

#     0
#   7   1
# 6       2
#   5   3
#     4

temp = [list(sys.stdin.readline().strip()) for _ in range(4)]
tables = [deque([]), deque([]), deque([]), deque([])]
for t in range(len(temp)):
    for i in temp[t]:
        if i == "0":
            tables[t].append(0)
        elif i == "1":
            tables[t].append(1)
k = int(sys.stdin.readline())
order = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for n, d in order:
    global direction, turn

    if n == 1:
        turn = [1, 0, 0, 0]
        direction = [d, -d, d, -d]
        if tables[0][2] != tables[1][6]:
            turn[1] = 1
            if tables[1][2] != tables[2][6]:
                turn[2] = 1
                if tables[2][2] != tables[3][6]:
                    turn[3] = 1
    elif n == 2:
        turn = [0, 1, 0, 0]
        direction = [-d, d, -d, d]
        if tables[0][2] != tables[1][6]:
            turn[0] = 1
        if tables[1][2] != tables[2][6]:
            turn[2] = 1
            if tables[2][2] != tables[3][6]:
                turn[3] = 1
    elif n == 3:
        turn = [0, 0, 1, 0]
        direction = [d, -d, d, -d]
        if tables[1][2] != tables[2][6]:
            turn[1] = 1
            if tables[0][2] != tables[1][6]:
                turn[0] = 1
        if tables[2][2] != tables[3][6]:
            turn[3] = 1
    elif n == 4:
        turn = [0, 0, 0, 1]
        direction = [-d, d, -d, d]
        if tables[2][2] != tables[3][6]:
            turn[3] = 1
            if tables[1][2] != tables[2][6]:
                turn[2] = 1
                if tables[0][2] != tables[1][6]:
                    turn[1] = 1

    for i in range(4):
        if turn[i] == 1:
            if direction[i] == 1:
                tables[i].appendleft(tables[i].pop())
            elif direction[i] == -1:
                tables[i].append(tables[i].popleft())

print(tables[0][0] + 2 * tables[1][0] + 4 * tables[2][0] + 8 * tables[3][0])
