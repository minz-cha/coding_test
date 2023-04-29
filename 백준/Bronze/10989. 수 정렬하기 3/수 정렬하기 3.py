import sys

N = int(input())
arr = [0]*10001

for i in range(N):
    a = int(sys.stdin.readline())
    arr[a] += 1
    
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)