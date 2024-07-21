import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])

people = []
for i in range(1, n + 1):
    age, name = data[i].split()
    age = int(age)
    people.append((age, name, i))

people.sort(key=lambda x: (x[0], x[2]))

for person in people:
    print(person[0], person[1])
