n = int(input())

for i in range(n):
    a = input().split()
    count = int(a[0]) #반복횟수
    str1 = a[1] #입력한 문자열
    str2 = [] #결과값 저장할 변수

    for j in range(len(str1)):
        str2.append((str1[j])*count)
    result = ''.join(str2)
    print(result)