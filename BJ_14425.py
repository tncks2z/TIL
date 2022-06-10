n,m = map(int, input().split())
S = dict()
cnt = 0
for _ in range(n):
    string = input()
    S[string] = True
for _ in range(m):
    examine = input()
    if examine in S.keys():
        cnt += 1
print(cnt)