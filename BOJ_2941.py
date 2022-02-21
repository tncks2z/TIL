croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()
for w in croatia:
    if w in word:
        word = word.replace(w,'a')
print(len(word))