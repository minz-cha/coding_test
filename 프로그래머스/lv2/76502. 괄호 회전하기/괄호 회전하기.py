def check(arr):
    stack = []
    openside = ['(', '{', '[']

    for i in arr:
        if i in openside:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            if i == '}' and stack[-1]== '{':
                stack.pop()
            if i == ']' and stack[-1] == '[':
                stack.pop()

    if len(stack) > 0:
        return False
    return True
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s) == True:
            answer += 1
        s = s[1:len(s)]+s[:1]
    
    return answer