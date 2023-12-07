def get_divisor(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors += 2 if i * i != n else 1
    return divisors

def solution(number, limit, power):
    answer = 0
    count = 0
    count_array = []
    for i in range(1, number+1):
        count = get_divisor(i)
        count_array.append(count) #약수의 개수 배열
        
    for i in range(len(count_array)):
        if limit >= count_array[i]:
            continue
        else:
            count_array[i] = power
    
    answer = sum(count_array)
    return answer