s = str(input())
if len(s) == 1:
    s = '0'+ s

count = 0
n = s

while(True):
    a = str(s) 
    s = int(s[0])+int(s[1])
    if len(str(s)) > 1: 
        s = s % 10 
    s = a[1] + str(s)
    count += 1

    if s == n:
        break
    
print(count)