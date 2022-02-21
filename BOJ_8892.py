t = int(input())

cnt = 0

for i in range(t):
    k = int(input())
    word_lst = [input() for j in range(k)]
    
    new_word_lst = []
    for a in range(len(word_lst)):
        for b in range(len(word_lst)):
            if a != b:
                new_word = word_lst[a]+word_lst[b]
                new_word_lst.append(new_word)
    
    palindrome_lst = []
    for c in range(len(new_word_lst)):
        if new_word_lst[c] == new_word_lst[c][::-1]:
            palindrome = new_word_lst[c]
            palindrome_lst.append(palindrome)

    if len(palindrome_lst) == 0 :
        print(0)
    else:
        print(palindrome_lst[0])