# coding=utf-8
# War -> Tests -> Main

import main

def test_play_turn_human_win():
    h_hand = [(2,), (5,), (8,), (12,)]
    c_hand = [(8,), (4,), (10,), (2,)]
    results = main.play_turn(h_hand, c_hand, [], [], [])
    (h_hand, c_hand, h_reserve, c_reserve) = results
    assert len(h_hand) == 3
    assert len(c_hand) == 3
    assert len(h_reserve) == 2
    assert len(c_reserve) == 0

def test_play_turn_human_win():
    h_hand = [(2,), (5,), (8,), (2,)]
    c_hand = [(8,), (4,), (10,), (11,)]
    results = main.play_turn(h_hand, c_hand, [], [], [])
    (h_hand, c_hand, h_reserve, c_reserve) = results
    assert len(h_hand) == 3
    assert len(c_hand) == 3
    assert len(h_reserve) == 0
    assert len(c_reserve) == 2

def test_play_turn_war():
    h_hand = [(2,), (5,), (8,), (2,), (7,), (1,), (1,)]
    c_hand = [(8,), (4,), (10,), (11,), (7,), (4,), (1,)]
    results = main.play_turn(h_hand, c_hand, [], [], [])
    (h_hand, c_hand, h_reserve, c_reserve) = results
    assert len(h_hand) == 2
    assert len(c_hand) == 2
    assert len(h_reserve) == 0
    assert len(c_reserve) == 10

def test_play_turn_double_war():
    h_hand = [(2,), (5,), (8,), (2,), (7,), (1,), (10,), (5,), (3,)]
    c_hand = [(8,), (4,), (10,), (11,), (7,), (4,), (1,), (5,), (3,)]
    results = main.play_turn(h_hand, c_hand, [], [], [])
    (h_hand, c_hand, h_reserve, c_reserve) = results
    assert len(h_hand) == 0
    assert len(c_hand) == 0
    assert len(h_reserve) == 0
    assert len(c_reserve) == 18
