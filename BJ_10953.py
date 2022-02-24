T = int(input())
num_lst = []

for i in range(T):
    a, b = map(int,input().split(","))
    sum = a + b
    num_lst.append(sum)

for num in num_lst:
    print(num)