import sys

block1 = [[1, 1, 1, 1]]
block2 = [[1], [1], [1], [1]]
block3 = [[1, 1], [1, 1]]
block4 = [[1, 0], [1, 0], [1, 1]]
block5 = [[0, 0, 1], [1, 1, 1]]
block6 = [[1, 1], [0, 1], [0, 1]]
block7 = [[1, 1, 1], [1, 0, 0]]
block8 = [[1, 0], [1, 1], [0, 1]]
block9 = [[0, 1, 1], [1, 1, 0]]
block10 = [[1, 0], [1, 1], [1, 0]]
block11 = [[0, 1, 0], [1, 1, 1]]
block12 = [[0, 1], [1, 1], [0, 1]]
block13 = [[1, 1, 1], [0, 1, 0]]
block14 = [[0, 1], [0, 1], [1, 1]]
block15 = [[1, 1, 1], [0, 0, 1]]
block16 = [[1, 1], [1, 0], [1, 0]]
block17 = [[1, 0, 0], [1, 1, 1]]
block18 = [[0, 1], [1, 1], [1, 0]]
block19 = [[1, 1, 0], [0, 1, 1]]

blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
for block in blocks:
    X, Y = n - len(block) + 1, m - len(block[0]) + 1
    for x in range(X):
        for y in range(Y):
            cnt = 0
            for i in range(len(block)):
                for j in range(len(block[0])):
                    if block[i][j] == 1:
                        cnt += board[x + i][y + j]
            result = max(result, cnt)
print(result)