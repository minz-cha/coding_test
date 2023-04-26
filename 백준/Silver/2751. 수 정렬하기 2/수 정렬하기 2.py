import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

res = sorted(arr)
print('\n'.join(map(str, res)))