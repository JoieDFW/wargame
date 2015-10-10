#!/usr/bin/python3
# coding=utf-8
# War -> Main

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
        print("\tTOTALS\tH {} + {}\tC {} + {}".format(
            len(h_hand), len(h_reserve), len(c_hand), len(c_reserve)))

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
    This function DOES modify all arguments in place. """

    # XXX Ugh someone please put this code out of its misery
    if len(h_hand) < 1 and len(h_reserve) < 1:
        raise cards.OutOfCardsError
    elif len(h_hand) < 1 and len(h_reserve) >= 1:
        (h_hand, h_reserve) = cards.flip_reserve(h_hand, h_reserve)

    if len(c_hand) < 1 and len(c_reserve) < 1:
        raise cards.OutOfCardsError
    elif len(c_hand) < 1 and len(c_reserve) >= 1:
        (c_hand, c_reserve) = cards.flip_reserve(c_hand, c_reserve)

    h_card = cards.pull_top(h_hand)
    c_card = cards.pull_top(c_hand)
    pot.extend([h_card, c_card])

    winner = cards.compare_cards(h_card, c_card)
    if winner == -1:  # Human wins
        print("{} > {} --- You win this round.".format(h_card, c_card))
        print("You win {} cards!".format(len(pot)))
        #print(" WIN", end="")
        h_reserve.extend(pot)

    elif winner == 1:  # Computer wins
        print("{} > {} --- You lose this round.".format(c_card, h_card))
        print("You lose {} cards!".format(len(pot)))
        #print("LOSE", end="")
        c_reserve.extend(pot)

    elif winner == 0:  # A tie; a cause for WAR!
        print("There is a tie.")
        #print(" TIE", end="")

        if len(h_hand) < 3 and len(h_reserve) < 3:
            raise cards.OutOfCardsError
        elif len(h_hand) < 3 and len(h_reserve) >= 3:
            (h_hand, h_reserve) = cards.flip_reserve(h_hand, h_reserve)

        if len(c_hand) < 3 and len(c_reserve) < 3:
            raise cards.OutOfCardsError
        elif len(c_hand) < 3 and len(c_reserve) >= 3:
            (c_hand, c_reserve) = cards.flip_reserve(c_hand, c_reserve)

        pot.extend(cards.pull_three(h_hand))
        pot.extend(cards.pull_three(c_hand))

        # Weeeee, recursion!
        play_turn(h_hand, c_hand, h_reserve, c_reserve, pot)
    else:
        assert False, "Panic!"

    return (h_hand, c_hand, h_reserve, c_reserve)

if __name__ == '__main__': main(h_hand, c_hand, [], [])
