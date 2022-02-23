n,m = int(input().split())

num_lst_1 = [list(map(int, input().split())) for _ in range(n)]
num_lst_2 = [list(map(int, input().split())) for _ in range(n)]

result = [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        result[i][j] = num_lst_1[i][j] * num_lst_2[i][j]

print(result)