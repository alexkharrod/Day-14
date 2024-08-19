import random

import art

# TODO 1 - create 2 lists - 1 for you and 1 for dealer
# TODO 2 - append your dealt cards with random
# TODO 3 - show you your cards and your total.  show only 1 of the dealer cards.

# TODO 4 - Ask if you want to hit or Stay and append cards and show accordingly ( slice dealers list 1:)

# TODO 5 - Work out logic - dealer hits on anything < 17
# TODO 6 - Ace value is 1 or 11 depending if you bust or are over ?? 17 ???

# TODO 7 - Highest Score without busting wins
#
# TODO 8 - Announce winner and scores and your score if you lose.( YOU BUSTED, or your lose?)

# TODO 9 - Add art and check everything

# TODO 10 - Create a game condition that interrupts gameplay when you or the dealer bus, or neither takes a card.

def main():
    """ This is the main game loop that runs the game. deals original hand, and checks for blackjack"""
    print(art.logo)
    print("Welcome to BLACKJACK!")
    game_over = False
    while game_over == False:
        for deal in range(2):
            #deal the cards
            dealer_hand.append(random.choice(cards))
            player_hand.append(random.choice(cards))

        # if dealer has black jack dealer wins
        if sum(dealer_hand) == 21 and len(dealer_hand) == 2:
            print(f"Dealer WINS!  BlackJack!")
            print(f"The Dealer's hand is : {dealer_hand}, which equals {len(dealer_hand)}")
            print(f"Your hand was {player_hand}, total score {sum(player_hand)}")

        #if dealer doesnt have 21 but player does, player wins.
        elif sum(dealer_hand) < 21 and sum(player_hand) == 21:
            print(f"BlackJack! YOU WIN!")
            print(f"The Dealers hand was {dealer_hand}")
            print(f"Your hand was {player_hand}, total score {sum(player_hand)}")
        else:
            # ask the player if they want to hit and calculate the winner
            print(f"The Dealers showing card is {dealer_hand[0]}.")
            player_play(player=player_hand, dealer=dealer_hand)
            # dealer_play(player_hand, dealer_hand)


# def hit(hand):
#     hand.append(random.choice(cards))


def player_play(player, dealer):
    """ this function asks if you want to hit and shows your cards and the dealer showing card and calculates winner"""
    player_turn = True
    while player_turn:
        hitme = input(f"Your cards are {player}, and your total is {sum(player)}\nDo you want to hit?  'y' for yes,"
                    f" 'n' for no.").title()
        if hitme == 'y':
            player.append(random.choice(cards))
            print(f"The Dealers showing card is {dealer[0]}.")
        elif hitme == 'n':
            player_turn = False
    # if sum(player) > 21 and 11 not in player:
    #     print(f"You Busted.  You Lost.  Your hand is: {player} and the total is {sum(player)}.")
    #     game_over = True
    #
    # elif sum(player) > 21 and 11 in player:
    #     for index in range(len(player)):
    #         if player[index] == 11:
    #             player[index] = [1]

# def dealer_play(player, dealer):
#     dealer_turn = True
#     while dealer_turn:
#         if sum(dealer) < 17:
#             hit(dealer_hand)


        #end the game if dealer busts













cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []


if __name__ == "__main__":
    main()

    print("Thanks for Playing!")