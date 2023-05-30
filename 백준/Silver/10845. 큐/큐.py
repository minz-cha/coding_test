import sys

n = int(sys.stdin.readline())
que = []

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == "push": que.append(s[1])
        
    elif s[0] == "pop":
        if que : print(que.pop(0))
        else: print("-1")
        
    elif s[0] == "size": print(len(que))
        
    elif s[0] == "empty":
        if len(que) == 0: print("1")
        else: print("0")
        
    if s[0] == "front":
        if len(que) == 0: print("-1")
        else: print(que[0])
        
    elif s[0] == "back":
        if len(que) == 0: print("-1")
        else: print(que[-1])