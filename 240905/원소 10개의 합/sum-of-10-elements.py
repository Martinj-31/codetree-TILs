integers = list(map(int, input().split()))

total = 0
for i in range(len(integers)):
    total += integers[i]

print(total)