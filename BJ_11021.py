T = int(input())
num_lst = []

for i in range(T):
    a, b = map(int, input().split())
    num_sum = a+b
    num_lst.append(num_sum)

for i,num in enumerate(num_lst):
    print(f"Case #{i+1}: {num}")