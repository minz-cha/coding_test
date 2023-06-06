n = int(input())
dp = [0] * 1000
dp[0] = 0
dp[1] = 1
dp[2] = 3

if n == 1 or n == 2:
    print(dp[n])

elif n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
        dp.append(dp[i])
    print (dp[n]%10007)