num_lst = [int(input()) for i in range(9)]
max_num = max(num_lst)
print(max_num, num_lst.index(max_num) + 1, sep = "\n")