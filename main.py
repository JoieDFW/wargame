#!/usr/bin/python3

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

DISABLE_WAIT = False

deck = cards.create_deck()
deck = cards.shuffle_cards(deck)
(hum, cpu) = cards.deal_cards(deck)
hreserve = []
creserve = []
win = False

interface.wait_for_input(DISABLE_WAIT)

while True:
    h = cards.get_top_card(hum)
    c = cards.get_top_card(cpu)
    
    result = cards.compare_cards(h, c)
    interface.output("You draw {}, and your opponent shows {}.".format(h, c))
    pot = [h, c]
    
    if result == -1:
        interface.output("{} > {} --- You win this round.".format(h, c))
        hreserve.extend(pot)
    elif result == 1:
        interface.output("{} > {} --- You lose this round.".format(c, h))
        creserve.extend(pot)
    elif result == 0:
        interface.output("There is a tie.")
        creserve.extend(pot)
    else:
        assert False, "You dun goofed"

    interface.wait_for_input(DISABLE_WAIT)  # Set at the top of the script

    if len(hum) < 1:
        if len(hreserve) > 0:
            hum = cards.shuffle_cards(hreserve)
            hreserve = []
        else:
            win = False
            break
    if len(cpu) < 1:
        if len(creserve) > 0:
            cpu = cards.shuffle_cards(creserve)
            creserve = []
        else:
            win = True
            break

if win:
    interface.output("You win! Well Done!")
else:
    interface.output("Sorry, you lost!")


