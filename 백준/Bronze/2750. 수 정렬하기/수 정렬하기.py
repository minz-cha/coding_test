N = int(input())
arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

res = ' '.join(str(num) for num in sorted(arr))
print(res)