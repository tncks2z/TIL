n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

# 시작 시간으로 먼저 오름차순
meetings = sorted(meetings, key=lambda x: x[0])
# 그 다음 끝나는 시간으로 오름차순
meetings = sorted(meetings, key=lambda x: x[1])

cnt = 0
last = 0

for op,ed in meetings:
    if op >= last:
        cnt += 1
        last = ed

print(cnt)