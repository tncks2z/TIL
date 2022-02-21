T = int(input())
num_lst = []
for i in range(T):
    a, b = map(int, input().split())
    num_lst.append(a + b)
for num in num_lst:
    print(num)