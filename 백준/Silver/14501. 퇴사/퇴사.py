n = int(input())
t = []
p = []
sum_ = []

for i in range(n):
    a,b= map(int, input().split())

    t.append(a)
    p.append(b)
    sum_.append(b)
sum_.append(0)

for i in range(n-1, -1, -1):
    if t[i] + i > n:
        sum_[i] = sum_[i + 1]
    else:
        sum_[i] = max(sum_[i + 1], p[i] + sum_[i + t[i]])

print(sum_[0])