import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input()) #테스트 케이스 개수
for i in range(t):
    n = int(input())
    a = n//2
    b = n-a

    while True:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1