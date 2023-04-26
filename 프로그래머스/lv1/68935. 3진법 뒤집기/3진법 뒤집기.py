def solution(n):
    answer = 0
    arr = []
    
    # 3진법 (앞뒤 반전)
    while (n > 0):
        a = n % 3
        n = n // 3
        arr.append(a)
    
    #리스트 형태 없애고 일반 문자열로 나타내기
    num_10 = str(''.join(str(i) for i in arr))
    answer = int(num_10,3) # 10진법으로
    
    return answer