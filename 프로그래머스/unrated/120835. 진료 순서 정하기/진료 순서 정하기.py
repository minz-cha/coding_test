def solution(emergency):
    answer = []
    temp = emergency.copy()
    emergency.sort(reverse=True)
    
    for i in temp:
        index = emergency.index(i)
        answer.append(index + 1)
    return answer