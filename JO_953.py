word = input().split()
player2foul = {}

for i in range(len(word)):
    if word[i] not in player2foul:
        player2foul[word[i]] = 1
    else:
        player2foul[word[i]] += 1

min_foul = min(player2foul.values())

for player in player2foul:
    if player2foul[player] == min_foul:
        print(player)
print(min_foul)