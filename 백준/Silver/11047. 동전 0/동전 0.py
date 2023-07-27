n, k = map(int, input().split(' '))
arr = []
count = 0

for i in range(n):
    a = int(input())
    arr.append(a)

# arr중 큰 값부터 확인
for i in range(n-1,-1,-1):
    if k%arr[i] != k:
        count += k//arr[i]
        k = k%arr[i]
    if k == 1:
        count += 1
        break
print(count)