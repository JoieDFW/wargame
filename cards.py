import random

#Tested
def create_deck():
    """Generates a standard set of 52 playing cards"""
    deck = []
    for number in range(1, 53):
        deck.append((number % 13) +1)
    return deck

#Tested
def shuffle_cards(deck):
    """Shuffles playing cards into a random order"""
    shuff = deck[:]
    random.shuffle(shuff)
    return shuff

#Tested
def deal_cards(deck):
    """Deals cards to the players one by one until cards run out"""
    hum = []
    cpu = []
    for (c, i) in zip(deck, range(1, 53)):
        if i % 2 == 0:
            hum.append(c)
        else:
            cpu.append(c)
    return (hum, cpu)

#Tested
def get_top_card(hand, n=1):
    """Pulls a single card by default, or 3 cards in war mode
    """
    if n > 1: 
        cs = []
        for i in range(n):
            cs.append(hand.pop())
        return cs
    else:
        return hand.pop()

#Tested
def compare_cards(hc, cc):
    """Compares the values of the cards to determine the winner 
    of the round
    -1 is a win for human player, 1 is for computer, 0 is tie"""
    if hc == 1:
        hc = 14
    if cc == 1:
        cc = 14
    if hc > cc:
        return -1
    elif cc > hc:
        return 1
    elif hc == cc:
        return 0
