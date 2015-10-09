
import cards

def test_create_deck():
    deck = cards.create_deck()
    assert type(deck) is list
    assert len(deck) == 52
    for card in deck:
        assert card <= 13
        assert card >= 1

def test_shuffle():
    deck = cards.create_deck()
    shuf = cards.shuffle_cards(deck)
    assert deck != shuf

def test_deal_cards():
    deck = cards.create_deck()
    inDeck = deck[:]
    (hum, cpu) = cards.deal_cards(inDeck)
    assert len(hum) == 26
    assert len(cpu) == 26
    assert deck == inDeck

def test_get_top_card():
    r_deck = cards.create_deck()
    deck = r_deck[:]
    card = cards.get_top_card(deck)
    assert card == r_deck[-1]
    assert r_deck != deck

def test_get_top_card_multiple():
    r_deck = cards.create_deck()
    deck = r_deck[:]
    hand = cards.get_top_card(deck, n=3)
    assert len(hand) == 3
    assert type(hand) is list
    assert r_deck != deck
    
def test_compare_cards_normal_usage():
    assert cards.compare_cards(4, 7) == 1
    assert cards.compare_cards(9, 7) == -1
    assert cards.compare_cards(5, 5) == 0
    assert cards.compare_cards(1, 5) == -1
    assert cards.compare_cards(13, 1) == 1
    assert cards.compare_cards(1, 1) == 0
