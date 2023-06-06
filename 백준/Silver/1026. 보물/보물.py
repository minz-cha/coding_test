n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a = sorted(a)
temp_b = b
sum_ = 0

for i in range(n):
    sum_ += a[i] * temp_b[temp_b.index(max(temp_b))]
    temp_b.remove(max(temp_b))

print(sum_)
