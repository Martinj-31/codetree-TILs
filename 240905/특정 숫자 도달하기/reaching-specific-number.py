integers = list(map(int, input().split()))

total = 0
cnt = 0
for i in range(len(integers)):
    if integers[i] >= 250:
        break
    else:
        total += integers[i]
        cnt += 1
print(total, total/cnt)