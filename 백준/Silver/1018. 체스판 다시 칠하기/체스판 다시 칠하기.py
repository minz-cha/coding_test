m, n = map(int, input().split())
board = []
result = []

for _ in range(m):
    board.append(input())

for i in range(m - 7):
    for j in range(n - 7):
        first_B = 0
        first_W = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    # i+j과 a+b의 값 차이가 짝수일 경우 같은 값을 가짐
                    if board[a][b] != 'B':
                        first_B += 1
                    if board[a][b] != 'W':
                        first_W += 1
                else:
                    if board[a][b] != 'W':
                        first_B += 1
                    if board[a][b] != 'B':
                        first_W += 1

        result.append(first_B)
        result.append(first_W)

print(min(result))