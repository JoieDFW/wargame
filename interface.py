# coding=utf-8
# War -> Interface

# XXX Deprecated
def display_hand(hum, cpu):
    print("Your card is {}! Computer's card is {}!".format(hum, cpu))


# Tested
def output(string="", outFn=print):
    """Print a message to the user. The print function can be overridden
    for testing, logging, or alternative interfaces."""

    outFn(string, end="")


# Tested
def wait_for_input(disabled=False, prompt=">>> "):
    """Return nothing only after user input.
    Function can be disabled by argument for testing purposes."""

    if not disabled: input(prompt)


# On hold until we can come to a consensus on how to represent suits
def unicode_repr(card):
    """Return the unicode character for a given card.
    If only a suit is given, return the suit's symbol.
    """

    return None
