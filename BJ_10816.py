n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
answer = {}

for number in numbers:
    if number in answer:
        answer[number] += 1
    else:
        answer[number] = 1
print(' '.join(str(answer[card]) if card in answer else '0' for card in cards))