alphabet2num = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
               }

word = list(input())

result = 0
for alphabet in word:
    for alphabet_set in alphabet2num:
        if alphabet in alphabet_set:
             num = alphabet2num[alphabet_set] + 1
    result += num
print(result)