# 슬라이싱 사용
s = input()
if s == s[::-1]:
    print(1)
else:
    print(0)


# 반복문만 사용
word = input()
cnt = 0

for i in range(len(word)):
    if word[i]==word[len(word)-1-i]:
        cnt += 1
    else:
        cnt += 0
if cnt == len(word):
    print(1)
else:
    print(0)