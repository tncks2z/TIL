t = int(input())

for i in range(t):
    num, word = input().split()
    num = int(num)
    change_word = ""
    for j in word:
        change_word += j*num
    print(change_word)