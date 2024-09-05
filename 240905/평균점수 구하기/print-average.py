score = list(map(float, input().split()))

total = 0
for i in score:
    total += i
    
print(round(total/len(score), 1))