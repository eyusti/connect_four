import pytest
from connect_four import Board, Game

def test_board_is_full_with_full_board():
    new_board = Board()
    new_board.board = [["R" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == True

def test_board_is_full_with_not_full_board():
    new_board = Board()
    new_board.board = [["?" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == False

def test_position_is_empty_while_empty():
    new_board = Board()
    new_board.board = [["?" for column in range(7)]for row in range(6)]
    assert new_board.is_position_empty(1,1) == True

def test_position_is_empty_while_full():
    new_board = Board()
    new_board.board = [["R" for column in range(7)]for row in range(6)]
    assert new_board.is_position_empty(1,1) == False

def test_place_works_correctly():
    new_board = Board()
    new_board.place(1,1,"R")
    assert new_board.board == [['?', '?', '?', '?', '?', '?', '?'],['?', "R", '?', '?', '?', '?', '?'],['?', '?', '?', '?', '?', '?', '?'],['?', '?', '?', '?', '?', '?', '?'],['?', '?', '?', '?', '?', '?', '?'],['?', '?', '?', '?', '?', '?', '?']]

def test_get_player_AI():
    game = Game()
    game.input = lambda: 'some input'

    game.get_player_AI()

    assert game.player1 != None and game.player2 != None