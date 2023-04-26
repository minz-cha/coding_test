def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: #제곱수면 약수의 개수가 홀수
            answer -= i
        else:
            answer += i
    return answer