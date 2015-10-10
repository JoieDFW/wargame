import random

class OutOfCardsError(Exception):
    pass

#Tested
def create_deck():
    """Generates a standard set of 52 playing cards"""
    deck = []
    for number in range(1, 53):
        deck.append((number % 13) +1)
    suit_1 = ["of Spades" for i in range(13)]
    suit_2 = ["of Diamonds" for i in range(13)]
    suit_3 = ["of Clubs" for i in range(13)]
    suit_4 = ["of Hearts" for i in range(13)]
    suits = suit_1 + suit_2 + suit_3 + suit_4
    assert len(suits) == 52
    return list(zip(deck, suits))

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

# Untested
def flip_reserve(hand, reserve):
    """Take the reserve cards into your hand after shuffling.
    This does NOT modify things in place!"""

    if (len(hand) + len(reserve)) < 1:
        raise Exception("What are you doing?")

    n_hand = hand[:]
    n_reserve = reserve[:]
    n_hand = shuffle_cards(n_reserve)
    n_reserve = []
    return (n_hand, n_reserve)

#Tested
def pull_top(hand, reserve, n=1):
    """Pull the top card from your hand. Flip reserve if there are not
    enough cards left. If there are not enough in the reserve either,
    throw OutOfCardsError."""
    #print("N = {}, HAND = {}, RESERVE = {}".format(n, len(hand), len(reserve)))
    if (len(hand)+len(reserve)) < 1:
        print("Arrgggh I'm all out!")
        raise OutOfCardsError()
    elif len(hand) < 1:
        (hand, reserve) = flip_reserve(hand, reserve)

    if n == 1:
        return hand.pop()
    else:
        return [hand.pop() for i in range(n)]

#Tested
def compare_cards(hc, cc):
    """Compares the values of the cards to determine the winner 
    of the round
    -1 is a win for human player, 1 is for computer, 0 is tie"""
    hc = hc[0]
    cc = cc[0]    
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
