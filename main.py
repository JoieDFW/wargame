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

IO = True
WAIT_FOR_INPUT = True

deck = cards.create_deck()
deck = cards.shuffle_cards(deck)
(hum, cpu) = cards.deal_cards(deck)
hreserve = []
creserve = []
win = False

interface.output()

while True:
    h = cards.get_top_card(hum)
    c = cards.get_top_card(cpu)
    
    result = cards.compare_cards(h, c)
    interface.display_hand(h, c)
    interface.output(wait=True)
    pot = [h, c]
    
    if result == -1:
        hreserve.extend(pot)
    elif result == 1:
        creserve.extend(pot)
    elif result == 0:
        creserve.extend(pot)
    else:
        assert False, "You dun goofed"

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
    print("You win! Well Done!")
else:
    print("Sorry, you lost!")


