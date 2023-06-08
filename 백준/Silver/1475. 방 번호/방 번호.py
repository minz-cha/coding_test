n = int(input())
n_list = list(map(int, str(n)))
arr = [0]*9

for i in n_list:
    if i != 9:
       arr[i] += 1
    if i == 9:
        arr[6] += 1

arr[6] = arr[6]/2 + arr[6]%2

print(int(max(arr)))