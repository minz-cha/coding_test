n = int(input())
numbers = [float(input()) for _ in range(n)]
# dp[i]는 i번째 원소까지 고려했을 때, 최대 연속 부분 곱
dp = [0.0] * n

# 초기값 설정
dp[0] = numbers[0]
max_product = dp[0]

for i in range(1, n):
    # i번째 원소를 포함하지 않는 경우, i번째 원소부터 새로 시작하는 경우 중 큰 값을 선택
    dp[i] = max(numbers[i], dp[i - 1] * numbers[i])
    max_product = max(max_product, dp[i])

print(f'{max_product:.3f}')
