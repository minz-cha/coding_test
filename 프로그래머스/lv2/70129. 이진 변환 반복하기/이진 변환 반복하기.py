def solution(s):
    answer = []
    cnt_0, count = 0, 0
    
    while s != '1':
        cnt_0 += s.count('0') #제거할 0의 갯수
        s = s.replace('0', '') 
        s = bin(len(s))[2:] #0 제거 후 길이에 대한 이진변환
        count += 1 #회차 수
    
    return (count, cnt_0)