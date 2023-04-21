w,h = map(int, input().split())

c = int(input()) #반복횟수
list1 = [0] #가로 자른 값 저장
list2 = [0] #세로 자른 값 저장

for i in range(c):
    a,b = map(int, input().split())
    if a == 0:
        list1.append(b)
    if a == 1:
        list2.append(b)
        
list1.append(h)
list2.append(w)
list1.sort() 
list2.sort()

def print_max(n):
    n_max = 0
    for i in range(len(n)-1):
        if n_max < n[i+1]-n[i]:
            n_max = n[i+1]-n[i]
    return n_max

a = print_max(list1)
b = print_max(list2)

print(a*b)