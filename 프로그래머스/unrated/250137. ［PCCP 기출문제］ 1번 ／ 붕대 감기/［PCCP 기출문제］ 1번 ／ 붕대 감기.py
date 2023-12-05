def control_health(num, max_):
    print("control")
    if num > max_:
        print("health", max_)
        return max_
    else:
        print("current", num)
        return num

def solution(bandage, health, attacks):
    current = health
    count = 0

    for i in range(1, attacks[-1][0] + 1):
        current_attack = 0
        attack_found = False
        
        for subattack in attacks:
            if i == subattack[0]:
                current_attack = subattack[1]
                attack_found = True
                break
    
        if attack_found:
            current -= current_attack
            count = 0
            if current < 0 or current == 0:
                return -1

        else: 
            count += 1
            if count == bandage[0]:
                current = current + bandage[1] + bandage[2]
                count = 0
            else:
                current += bandage[1]
        
        current = control_health(current, health)
                
    return current
