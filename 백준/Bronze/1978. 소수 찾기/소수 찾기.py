import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if is_prime(num):
        count += 1
print(count)