def distribute_hamburgers(n, k, s):
    s = list(s)
    
    # 최대로 먹을 수 있는 사람의 수
    count = 0
    
    # 사람 'P'와 햄버거 'H'의 위치를 기록할 리스트
    people = []
    hamburgers = []
    
    # 'P'와 'H'의 위치를 각각 기록
    for i in range(n):
        if s[i] == 'P':
            people.append(i)
        elif s[i] == 'H':
            hamburgers.append(i)
    
    # 포인터를 사용하여 각 사람에게 가까운 햄버거를 할당
    p_ptr = 0
    h_ptr = 0
    
    while p_ptr < len(people) and h_ptr < len(hamburgers):
        if abs(people[p_ptr] - hamburgers[h_ptr]) <= k:
            count += 1
            p_ptr += 1
            h_ptr += 1
        elif people[p_ptr] < hamburgers[h_ptr]:
            p_ptr += 1
        else:
            h_ptr += 1
    
    return count

n, k = map(int, input().split())
s = input().strip()

print(distribute_hamburgers(n, k, s))