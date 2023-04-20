num = input().split()
a = num[0]
b = num[1]
num1 = []
num2 = []

for i in range(3,0, -1):
    num1.append(a[i-1])
    num2.append(b[i-1])
    
num1 = int(''.join(num1))
num2 = int(''.join(num2))

print(max(num1, num2))