n = int(input())
grade = list(map(float, input().split()))

total = 0
for i in grade:
    total += i
n = total/len(grade)
print(round(n, 1))
if n >= 4.0:
    print("Perfect")
elif 4.0 > n >= 3.0:
    print("Good")
else: print("Poor")