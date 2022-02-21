word = input().upper()

ban_word = "Cambridge".upper()

for s in ban_word:
    if s in word:
        word = word.replace(s,"")
    else:
        pass
print(word)
