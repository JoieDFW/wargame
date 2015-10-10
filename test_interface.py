# coding=utf-8
# War -> Tests -> Interface

import interface

def test_unicode_repr(): 
    assert "Not implemented yet"


def test_wait_disabling():
    interface.wait_for_input(disabled=True)
    assert "If we reach this point it works!"

def test_pic_repr():
    butts = interface.pic_repr((2, "of Spades"))
    print(butts)
