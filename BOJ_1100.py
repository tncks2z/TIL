n,m = 8,8

chessboard = [list(map(str,input())) for _ in range(n)]
whiteboard = []

cnt = 0

for i in range(n):
    for j in range(n):
        if (i%2 == j%2) and (chessboard[i][j] == 'F'):
            cnt += 1

print(cnt)