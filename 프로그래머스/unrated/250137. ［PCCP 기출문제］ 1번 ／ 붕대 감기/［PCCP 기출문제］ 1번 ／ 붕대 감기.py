def control_health(num, max_):
    print("control")
    if num > max_:
        print("health", max_)
        return max_
    else:
        print("current", num)
        return num

def solution(bandage, health, attacks):
    current = health # 체력 초깃값
    count = 0 # 연속 성공

    for i in range(1, attacks[-1][0] + 1):
        current_attack = 0
        attack_found = False 
        
        for subattack in attacks:
            if i == subattack[0]: #시간 초와 공격시간 같은 경우
                current_attack = subattack[1]
                attack_found = True # 공격 받음
                break
    
        # 공격 받은 경우
        if attack_found:
            current -= current_attack 
            count = 0
            if current < 0 or current == 0:
                return -1

        # 공격 받지 않은 경우 - 회복
        else: 
            count += 1
            # 연속 회복 성공
            if count == bandage[0]:
                current = current + bandage[1] + bandage[2]
                count = 0
            else:
                current += bandage[1]
        
        # 회복한 체력이 최대 체력을 넘지 않도록 제어
        current = control_health(current, health)
                
    return current
