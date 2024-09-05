string = list(input().split())

for i in range(len(string)):
    print(string[len(string)-i-1], end="")