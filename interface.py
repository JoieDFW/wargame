# coding=utf-8
# War -> Interface

# Tested
def wait_for_input(disabled=False, prompt=">>> \n"):
    """Return nothing only after user input.
    Function can be disabled by argument for testing purposes."""

    if not disabled: input(prompt)


def unicode_repr(card):
    """Return the unicode character for a given card.
    If only a suit is given, return the suit's symbol.
    """
    if card[1] == "of Spades": return "♠"
    if card[1] == "of Clubs": return "♣"
    if card[1] == "of Diamonds": return "♦"
    if card[1] == "of Hearts": return "♥"

def string_repr(card): pass

def royal_number_switch(card):
    """Replace royal numbers (e.g. 11, 12, 13, 1) with their letters."""

    (n, s) = card
    subs = {1: "A", 11: "J", 12: "Q", 13: "K"}
    if n in subs.keys():
        card = (subs[n], s)
    return card


def pic_repr(card):
    """Return a string representing a given card."""
    (n, s) = royal_number_switch(card)
    displayNumber = str(n)
    displaySuit = unicode_repr(card)
    if len(displayNumber) == 1:
        displayNumber = "*" + displayNumber

    return [
        " ____ ",
        "|{}  |".format(displayNumber),  # should always be two chars
        "|    |",
        "|   {}|".format(displaySuit),
        "'----'"]
