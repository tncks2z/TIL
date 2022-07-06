n = int(input())
times = list(map(int, input().split()))

times = sorted(times)

result = 0
results = []
for time in times:
    result += time
    results.append(result)
    
print(sum(results))