n,m = map(int, input().split())
never_heard = {}
never_seen = {}

for i in range(n):
    word = input()
    never_heard[word] = 1

for j in range(m):
    word = input()
    never_seen[word] = 1

never_heard_seen = [person for person in never_heard if person in never_seen]
never_heard_seen = sorted(never_heard_seen)

print(len(never_heard_seen))
for i in range(len(never_heard_seen)):
    print(never_heard_seen[i])