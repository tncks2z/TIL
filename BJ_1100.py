n = 8

chessboard = [list(input()) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        if (i%2 == j%2) and (chessboard[i][j] == 'F'):
            cnt += 1

print(cnt)