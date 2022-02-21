T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    num_sum = a + b
    print(f"Case #{i+1}: {a} + {b} = {num_sum}")