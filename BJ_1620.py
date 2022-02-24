n,m = map(int,input().split())

poketmon2num = {}
num2poketmon = {}

for i in range(1,n+1):
    poketmon = input()
    if poketmon not in poketmon2num:
        poketmon2num[poketmon] = str(i)
        num2poketmon[str(i)] = poketmon
        
for j in range(m):
    WhoRU = input()
    if WhoRU in poketmon2num:
        print(poketmon2num[WhoRU])
    else:
        print(num2poketmon[WhoRU])