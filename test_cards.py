# coding=utf-8
# War -> Tests -> Cards

import pytest
import cards

def test_create_deck():
    deck = cards.create_deck()
    assert type(deck) is list
    assert len(deck) == 52
    for card in deck:
        assert type(card) is tuple
        assert type(card[0]) is int
        assert type(card[1]) is str
        assert card[0] <= 13
        assert card[0] >= 1

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

def test_flip_reserve():
    (hand, reserve) = ([], [(2,), (5,), (11,)])
    (n_hand, n_reserve) = cards.flip_reserve(hand, reserve)
    assert n_hand == [(2,), (5,), (11,)]
    assert n_reserve == []
    assert hand != n_hand
    assert reserve != n_reserve

def test_pull_top_card():
    deck = [(2,), (5,), (11,)]
    card = cards.pull_top(deck)
    assert len(deck) == 2
    assert card == (11,)

def test_pull_top_three():
    deck = [(2,), (5,), (11,)]
    cs = cards.pull_three(deck)
    assert len(deck) == 0
    assert type(cs) is list
    assert cs == [(11,), (5,), (2,)]

def test_pull_top_error():
    with pytest.raises(cards.OutOfCardsError):
        cards.pull_three([(3,)])
    
def test_compare_cards_normal_usage():
    assert cards.compare_cards((4,), (7,)) == 1
    assert cards.compare_cards((9,), (7,)) == -1
    assert cards.compare_cards((5,), (5,)) == 0
    assert cards.compare_cards((1,), (5,)) == -1
    assert cards.compare_cards((13,), (1,)) == 1
    assert cards.compare_cards((1,), (1,)) == 0
