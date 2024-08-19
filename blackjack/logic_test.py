player_hand = [2, 4, 3, 11]
print(player_hand)


for index in range(len(player_hand)):
    if player_hand[index] == 11:
        player_hand[index] = [1]
