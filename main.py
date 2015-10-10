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

DISABLE_WAIT = True
GAME_WON = False

deck = cards.create_deck()
deck = cards.shuffle_cards(deck)
(h_hand, c_hand) = cards.deal_cards(deck)

interface.wait_for_input(DISABLE_WAIT)

# Untested
def main(h_hand, c_hand, h_reserve, c_reserve):
    """Run the game."""

    while True:
        # NOTE Could be simpler...
        results = play_turn(h_hand, c_hand, h_reserve, c_reserve, [])
        (h_hand, c_hand, h_reserve, c_reserve) = results

        interface.wait_for_input(DISABLE_WAIT)  # Set at the top of the script

        # XXX Reserves need to be handled better
        if len(h_hand) < 1:
            if len(h_reserve) > 0:
                h_hand = cards.shuffle_cards(h_reserve)
                h_reserve = []
            else:
                GAME_WON = False
                break
        if len(c_hand) < 1:
            if len(c_reserve) > 0:
                c_hand = cards.shuffle_cards(c_reserve)
                c_reserve = []
            else:
                GAME_WON = True
                break

    # NOTE Global state is questionable practice~
    if GAME_WON:
        print("You win! Well Done!")
    else:
        print("Sorry, you lost!")


# Lightly Tested
def play_turn(h_hand, c_hand, h_reserve, c_reserve, pot):
    """Play one hand of the game. Call recursively to resolve ties.
    This function DOES modify all arguments.
    """

    h_card = cards.get_top_card(h_hand)
    c_card = cards.get_top_card(c_hand)
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

        # XXX I'm sensing a bug here...
        # What if a hand has less than three cards?
        # We need to handle reserves better.
        pot.extend(cards.get_top_card(h_hand, n=3))
        pot.extend(cards.get_top_card(c_hand, n=3))

        # Weeeee, recursion!
        results = play_turn(h_hand, c_hand, h_reserve, c_reserve, pot)
        (h_hand, c_hand, h_reserve, c_reserve) = results
    else:
        assert False, "Panic!"

    return (h_hand, c_hand, h_reserve, c_reserve)

if __name__ == '__main__': main(h_hand, c_hand, [], [])
