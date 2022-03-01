word_list = [input() for _ in range(5)]
word_len_list = [len(word) for word in word_list]

for i in range(max(word_len_list)):
    for word in word_list:
        if i < len(word):
            print(word[i],end="")