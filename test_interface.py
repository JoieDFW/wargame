# coding=utf-8
# War -> Tests -> Interface

import interface

def test_output():
    console = []
    interface.output("Butts", outFn=lambda s, end: console.append(s+end))
    assert "Butts" in console

def test_unicode_repr(): 
    assert "Not implemented yet"


def test_wait_disabling():
    interface.wait_for_input(disabled=True)
    assert "If we reach this point it works!"
