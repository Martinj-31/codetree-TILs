import sys

n = int(sys.stdin.readline())
customer = list(map(int, sys.stdin.readline().split()))
leader_max, member_max = map(int, sys.stdin.readline().split())

customer.sort()
cnt = 0
for i in customer:
    if leader_max >= i:
        cnt += 1
    elif leader_max < i:
        cnt += 1
        i -= leader_max
        if i % member_max > 0:
            cnt += i // member_max + 1
        else:
            cnt += i // member_max

print(cnt)
