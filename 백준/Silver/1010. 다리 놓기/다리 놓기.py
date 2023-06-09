import sys

c = int(sys.stdin.readline())
for i in range(c):
    a = 1
    b = 1
    n, m = map(int, sys.stdin.readline().split())
    for j in range(m-n+1, m+1):
        a *= j
    for k in range(1, n+1):
        b *= k
    print(int(a/b))