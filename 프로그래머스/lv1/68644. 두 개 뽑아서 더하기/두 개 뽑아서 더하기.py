def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if i != j:
                sum = numbers[i] + numbers[j]
                if sum in answer:
                    continue
                else:
                    answer.append(sum)
            
            else:
                   continue
    return sorted(answer)