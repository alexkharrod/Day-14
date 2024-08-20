import random

import art


def main():
    """ This is the main game loop that runs the game. deals original hand, and checks for blackjack"""

    # game_on = True
    # while game_on:
    print("Welcome to BLACKJACK!")
    dealer_hand = []
    player_hand = []
    for deal in range(2):
        # deal the cards
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))

    # if dealer has black jack dealer wins
    if sum(player_hand) == 22:
        #  Just change the first one. handle_aces(player_hand)
        player_hand[0] = 1

    if sum(dealer_hand) == 22:
        dealer_hand[0] = 1

    if sum(dealer_hand) == 21 and len(dealer_hand) == 2:
        print(f"Dealer WINS!  BlackJack!")

    # if dealer doesn't have 21 but player does, player wins.
    elif sum(dealer_hand) < 21 and sum(player_hand) == 21:
        print(f"BlackJack! YOU WIN!")

    else:
        # ask the player if they want to hit and calculate the winner
        print(f"The Dealer is showing: {dealer_hand[0]}.")
        player_play(player=player_hand, dealer=dealer_hand)
        if sum(player_hand) < 22:
            dealer_play(player=player_hand, dealer=dealer_hand)

        if sum(player_hand) < 22 and sum(dealer_hand) < 22:
            if sum(player_hand) == sum(dealer_hand):
                print("It's a draw!")
            elif sum(player_hand) > sum(dealer_hand):
                print("Player wins")
            elif sum(player_hand) < sum(dealer_hand):
                print("Dealer Wins")

    print(f"Player's hand: {player_hand} and total: {sum(player_hand)}\n"
          f"Dealer's hand: {dealer_hand} and total: {sum(dealer_hand)}")


def player_play(player, dealer):
    """ this function asks if you want to hit and shows your cards and the dealer showing card and calculates winner"""
    player_turn = True
    while player_turn:
        hit_me = input(f"Your cards are {player}, and your total is {sum(player)}\nDo you want to hit?  'y' for yes,"
                       f" 'n' for no.\n").lower()
        if hit_me == 'y':
            player.append(random.choice(cards))
            if sum(player) > 21 and 11 not in player:
                print(f"You Busted, Dealer Wins!")
                return

            elif sum(player) > 21 and 11 in player:
                handle_aces(player)

        elif hit_me == 'n':
            player_turn = False


def dealer_play(player, dealer):
    while sum(dealer) < 17:
        dealer.append(random.choice(cards))
        if sum(dealer) > 21 and 11 not in dealer:
            print(f"Dealer Busted, You Win!")
            return
        elif sum(dealer) > 21 and 11 in dealer:
            handle_aces(dealer)


def handle_aces(whose_hand):
    for index in range(len(whose_hand)):
        if whose_hand[index] == 11:
            whose_hand[index] = 1
        print(f"Counted {whose_hand} Aces as 1 instead of 11!")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


print(art.logo)
if __name__ == "__main__":
    game_on = True
    while game_on:
        main()
        play_again = input("Would you like to play again? 'y for yes, 'n' for no.").lower()
        if play_again == 'y':
            print("\n" * 20)
        else:
            game_on = False
            break
print("Thanks for Playing!")