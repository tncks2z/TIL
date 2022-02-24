n = int(input())
line = "* " * n

for i in range(n):
    print(line)
    line = line[::-1]