n,m = int(input().split())

num_lst_1 = [list(map(int, input().split())) for i in range(n)]
num_lst_2 = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(num_lst_1[i][j] * num_lst_2[i][j],end=" ")
    print()
