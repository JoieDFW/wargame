# coding=utf-8
# War -> Interface
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


def string_repr(card):
    """Return a string representing a given card."""

    return None
