#!/usr/bin/python3
# coding=utf-8
# War -> Main

#Create a deck of 52 standard playing cards
#Shuffle the deck
#Deal half the cards to each player, one by one
#In each turn, each opponent flips their top card
#If the cards are the same number, war mode must activate
#In war mode, each player places down their 3 cards on top
#Then they flip a fourth card to see who wins the "pot"
#Whoever wins the pot gets all cards in the pot
#Won cards go into a reserve pile, separate from main cards
#If main cards run out, the reserve gets shuffled and becomes main
#Game continues until one player runs out of cards in main and reserve

import cards
import interface

exampleCards = cards.create_deck()
for card in exampleCards:
    picture = interface.pic_repr(card)
    for line in picture:
        print(line)
    print()

DISABLE_WAIT = True

deck = cards.create_deck()
deck = cards.shuffle_cards(deck)
(h_hand, c_hand) = cards.deal_cards(deck)

interface.wait_for_input(DISABLE_WAIT)

# Untested
def main(h_hand, c_hand, h_reserve, c_reserve):
    """Run the game."""

    while True:
        # NOTE Could be simpler...
        try:
            results = play_turn(h_hand, c_hand, h_reserve, c_reserve, [])
            (h_hand, c_hand, h_reserve, c_reserve) = results
        except cards.OutOfCardsError:
            break

        interface.wait_for_input(DISABLE_WAIT)  # Set at the top of the script

    if len(h_hand) > len(c_hand):
        print("You win! Well Done!")
    else:
        print("Sorry, you lost!")


# Tested
def play_turn(h_hand, c_hand, h_reserve, c_reserve, pot):
    """Play one hand of the game. Call recursively to resolve ties.
    This function DOES modify all arguments.
    """

    h_card = cards.pull_top(h_hand, h_reserve)
    c_card = cards.pull_top(c_hand, c_reserve)
    pot.extend([h_card, c_card])

    winner = cards.compare_cards(h_card, c_card)
    if winner == -1:  # Human wins
        print("{} > {} --- You win this round.".format(h_card, c_card))
        print("You win {} cards!".format(len(pot)))
        h_reserve.extend(pot)

    elif winner == 1:  # Computer wins
        print("{} > {} --- You lose this round.".format(c_card, h_card))
        print("You lose {} cards!".format(len(pot)))
        c_reserve.extend(pot)

    elif winner == 0:  # A tie; a cause for WAR!
        print("There is a tie.")
        pot.extend(cards.pull_top(h_hand, h_reserve, n=3))
        pot.extend(cards.pull_top(c_hand, c_reserve, n=3))

        # Weeeee, recursion!
        results = play_turn(h_hand, c_hand, h_reserve, c_reserve, pot)
        (h_hand, c_hand, h_reserve, c_reserve) = results
    else:
        assert False, "Panic!"

    return (h_hand, c_hand, h_reserve, c_reserve)

if __name__ == '__main__': main(h_hand, c_hand, [], [])
