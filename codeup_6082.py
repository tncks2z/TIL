# 369 게임의 왕이 되어보자
n = int(input())

for i in range(1, n+1):
    if i%10 == 3 or i%10 == 6 or  i%10 == 9:
        i = "X"
    print(i, end = " ")