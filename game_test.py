import pytest
import math
from connect_four import Board, Game, check_four_consecutive,check_potential_win

# Game AI Helpers
def test_get_opposite_symbol():
    game = Game()
    assert game.get_opposite_symbol("1") == "2"
    assert game.get_opposite_symbol("2") == "1"
    
def test_check_potential_win():
    assert check_potential_win(["1","2","2","?","2","2","1"])==["2","2"]

def test_heuristic_simple():
    game = Game()
    board = Board()
    game.set_heuristic_score = check_potential_win
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '2', '2', '?', '2', '2', '?'],
        ['?', '2', '2', '?', '2', '2', '?']]
    assert game.heuristic_score(board) == -4

def test_heuristic_complex():
    game = Game()
    board = Board()
    game.set_heuristic_score = check_potential_win
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '1', '?', '1', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '1', '?', '1', '1', '?'],
        ['?', '1', '1', '?', '1', '?', '?']]
    assert game.heuristic_score(board) == 5

def test_heuristic_is_diagonal_getting_double_counted():
    game = Game()
    board = Board()
    game.set_heuristic_score = check_potential_win
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '1', '?', '?', '?', '?', '?'],
        ['?', '?', '1', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '1', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?']]
    assert game.heuristic_score(board) == 1

def test_heuristic_is_diagonal_getting_double_counted_2():
    game = Game()
    board = Board()
    game.set_heuristic_score = check_potential_win
    board.board = [
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '?'],
        ['?', '?', '?', '?', '1', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?']]
    assert game.heuristic_score(board) == 1