from collections import deque

K, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(5)]

add_treasure = list(map(int, input().split()))
add_treasure = deque(add_treasure)


def check_array(array):
    for i in range(len(array)):
        print(array[i])


def rotate_grid(array, x, y, degree):
    for d in range(int(degree/90)):
        new_array = [[0] * 5 for _ in range(5)]
        rotate_array = [[0] * 3 for _ in range(3)]
        for i in range(5):
            for j in range(5):
                if x-1 <= i <= x+1 and y-1 <= j <= y+1:
                    rotate_array[i-x+1][j-y+1] = array[i][j]
                else:
                    new_array[i][j] = array[i][j]
        for i in range(3):
            for j in range(3):
                new_array[i+x-1][j+y-1] = rotate_array[3-j-1][i]
        array = new_array

    return new_array


def get_treasure(array, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    info_treasure = [(x, y)]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if array[nx][ny] == array[x][y] and visited[nx][ny] == False:
                visited[nx][ny] = True
                info_treasure.append((nx, ny))
                count += 1
                q.append((nx, ny))

    return count, info_treasure


def get_point(array):
    total_treasure = 0
    info_treasure = None
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            num_treasure, info_treasure = get_treasure(array, i, j, visited)
            if num_treasure >= 3:
                total_treasure += num_treasure
                for info in info_treasure:
                    array[info[0]][info[1]] = 0
            else:
                info_treasure = []

    return total_treasure, info_treasure


def check_point(array):
    total_treasure = 0
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            num_treasure, _ = get_treasure(array, i, j, visited)
            if num_treasure >= 3:
                total_treasure += num_treasure

    return total_treasure


def add(array):
    for i in range(5):
        for j in range(5):
            if array[4 - j][i] == 0:
                array[4 - j][i] = add_treasure.popleft()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

treasure_list = []
for k in range(K):
    # Check rotate
    max_treasure = 0
    best_treasure = 0
    best_grid = [0, 0]
    best_degree = None
    for degree in [270, 180, 90]:
        for i in range(3, 0, -1):
            for j in range(3, 0, -1):
                temp = rotate_grid(grid, i, j, degree)
                total_treasure, _ = get_point(temp)
                if best_treasure <= total_treasure:
                    best_treasure = total_treasure
                    best_grid[0], best_grid[1] = i, j
                    best_degree = degree

    if best_treasure == 0:
        break

    # Real trial
    grid = rotate_grid(grid, best_grid[0], best_grid[1], best_degree)

    while True:
        total_treasure, info_treasure = get_point(grid)
        max_treasure += total_treasure
        add(grid)
        if total_treasure == 0:
            break

    treasure_list.append(max_treasure)

for num in treasure_list:
    print(num, end=' ')