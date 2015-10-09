
deck = cards.create_deck()
deck = cards.shuffle_cards(deck)
(hum, cpu) = cards.deal_cards(deck)

while True:
    h = cards.get_top_card(hum)
    c = cards.get_top_card(cpu)
    
    result = cards.compare_cards(h, c)

    if result == -1:
        pass
    elif result == 1:
        pass
    elif result == 0:
        pass
    else:
        assert False, "Panic!"
