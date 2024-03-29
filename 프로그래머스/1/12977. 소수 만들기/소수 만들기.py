from itertools import combinations
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        sum_ = sum(i)
        if (is_prime_number(sum_)):
            answer += 1
    return answer