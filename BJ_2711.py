T = int(input())

for i in range(T):
    n,s = map(str,input().split())
    n = int(n)
    print(s[:n-1] + s[n:])