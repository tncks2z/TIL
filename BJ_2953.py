num_list = []

for i in range(5):
    a, b, c, d = map(int, input().split())
    num_sum = a + b + c + d
    num_list.append(num_sum)
    
print(num_list.index(max(num_list))+1, max(num_list))