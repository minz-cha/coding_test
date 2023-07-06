def solution(name):
    answer = 0
    move = len(name)-1
    
    for i, letter in enumerate(name):
        print(i, letter)
        # 알파벳 변경 횟수
        answer += min(ord(letter)-ord('A'), ord('Z')-ord(letter)+1)
        
        # 이동 횟수
        next_ = i+1
        while(next_ < len(name) and name[next_]=='A'):
            next_ += 1
        
        move = min([move, 2*i + len(name)-next_, i + 2*(len(name)-next_)])
    answer += move
    return (answer)