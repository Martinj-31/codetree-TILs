import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))


def dfs(depth, total, plus, minus, multiply):
    global maximum, minimum
    if depth == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1)


maximum = -1e9
minimum = 1e9
dfs(1, numbers[0], operator[0], operator[1], operator[2])
print(int(minimum), int(maximum))
