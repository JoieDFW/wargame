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
# XXX
TOTAL_TURNS = 0

# Untested
def main(human, cpu):
    """Run the game."""

    while True:
        print("\tTOTALS\t\tH {} + {}  \tC {} + {}".format(
            len(human[0]), len(human[1]), len(cpu[0]), len(cpu[1])))

        try:
            (human, cpu) = play_turn(human, cpu, [])
        except cards.OutOfCardsError:
            break

        interface.wait_for_input(DISABLE_WAIT)  # Set at the top of the script

    if len(human[0]) > len(cpu[0]):
        print("You win! Well done!")
        return True
    else:
        print("Sorry, you lost!")
        return False


# Untested
def flip_if_needed(player, n=1):
    (hand, reserve) = player
    if len(hand) < n:
        (hand, reserve)= cards.flip_reserve(hand, reserve)
    return (hand, reserve)


# Lightly Tested
def play_turn(human, cpu, pot):
    #XXX
    global TOTAL_TURNS
    TOTAL_TURNS += 1
    (h_hand, h_reserve) = flip_if_needed(human)
    (c_hand, c_reserve) = flip_if_needed(cpu)

    h_card = cards.pull_top(h_hand)
    c_card = cards.pull_top(c_hand)
    pot.extend([h_card, c_card])

    winner = cards.compare_cards(h_card, c_card)
    if winner == -1:  # Human wins
        #print("{} > {} --- You win this round.".format(h_card, c_card))
        #print("You win {} cards!".format(len(pot)))
        print(" WIN", end="")
        h_reserve.extend(pot)

    elif winner == 1:  # Computer wins
        #print("{} > {} --- You lose this round.".format(c_card, h_card))
        #print("You lose {} cards!".format(len(pot)))
        print("LOSE", end="")
        c_reserve.extend(pot)

    elif winner == 0:  # A tie; a cause for WAR!
        #print("There is a tie.")
        print(" TIE", end="\n")

        (h_hand, h_reserve) = flip_if_needed((h_hand, h_reserve), n=3)
        (c_hand, c_reserve) = flip_if_needed((c_hand, c_reserve), n=3)

        pot.extend(cards.pull_three(h_hand))
        pot.extend(cards.pull_three(c_hand))

        # Weeeee, recursion!
        ((h_hand, h_reserve), (c_hand, c_reserve)) = play_turn(
            (h_hand, h_reserve), (c_hand, c_reserve), pot)

    return ((h_hand, h_reserve), (c_hand, c_reserve))


if __name__ == '__main__':
    won_games = 0
    lost_games = 0
    for i in range(1000):
        deck = cards.create_deck()
        deck = cards.shuffle_cards(deck)
        (h_hand, c_hand) = cards.deal_cards(deck)

        interface.wait_for_input(DISABLE_WAIT)
        won = main((h_hand, []), (c_hand, []))
        if won:
            won_games += 1
        else:
            lost_games += 1

    print("Games won:  {}".format(won_games))
    print("Games lost: {}".format(lost_games))
    print("Total number of turns: {}".format(TOTAL_TURNS))
