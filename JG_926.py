num_lst_1 = [list(map(int, input().split())) for i in range(2)]
num_lst_2 = [list(map(int, input().split())) for i in range(2)]

result = [[0] * 4] * 2

for i in range(2):
    for j in range(4):
        result[i][j] = num_lst_1[i][j] * num_lst_2[i][j]
        
print(result)