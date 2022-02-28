n = int(input())

files = [input() for _ in range(n)]
pattern = ""

for columns in zip(*files):
    pattern += "?" if columns.count(columns[0]) < n else columns[0]
    
print(pattern)
