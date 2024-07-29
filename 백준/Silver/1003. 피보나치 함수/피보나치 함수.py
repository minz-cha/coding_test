def fibonacci_count(n):
    dp = [[0, 0] for _ in range(n + 1)]
    
    if n >= 0:
        dp[0] = [1, 0] 
    if n >= 1:
        dp[1] = [0, 1] 
    
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    
    return dp[n]

T = int(input())

for _ in range(T):
    N = int(input())
    result = fibonacci_count(N)
    print(result[0], result[1])