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

def flip_reserve(hand, reserve):
    """Take reserve into hand. Does not mutate inputs."""

    n_hand = hand[:]
    n_reserve = reserve[:]
    n_hand = shuffle_cards(n_reserve)
    return (n_hand, [])

#Tested
def pull_top(hand):
    """Return the top card from a hand.
    Throws OutOfCardsError if there are not enough cards to pull."""

    if len(hand) < 1:
        raise OutOfCardsError
    else:
        return hand.pop()


def pull_three(hand):
    """Return the top three cards of a given hand as a list.
    Throws OutOfCardsError if there are not enough cards to pull."""

    if len(hand) < 3:
        raise OutOfCardsError
    else:
        return [hand.pop() for i in range(3)]
        

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
