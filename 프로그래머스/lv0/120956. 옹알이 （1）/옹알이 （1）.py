def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        cnt = 0
        for word in words:
            if word in i:
                i = i.replace(word, ' ')
                cnt += 1

        if (len(i.replace(" ", "")) == 0) and (cnt > 0):
            answer += 1
    
    return answer