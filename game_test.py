import pytest
import math
from connect_four import Board, Game, check_four_consecutive,check_potential_win

# Game AI Test Cases
def test_minmax_winning_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?']]
    assert new_game.min_max(new_game.board, "1", 4) == math.inf

def test_minmax_losing_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '1', '1', '2', '?', '?']]
    assert new_game.min_max(new_game.board, "1", 4) == -math.inf

def test_minmax_tied_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['1', '2', '1', '2', '1', '2', '1'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert new_game.min_max(new_game.board, "1", 4) == 0

def test_minmax_maximizer_win():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['1', '1', '1', '2', '2', '2', '?'],
        ['2', '2', '2', '1', '1', '1', '?'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2']]
    assert new_game.min_max(new_game.board,"1", 4) == math.inf
    
def test_minmax_maximizer_lose():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['1', '1', '1', '2', '?', '2', '?'],
        ['2', '2', '2', '1', '?', '1', '?'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2']]
    assert new_game.min_max(new_game.board,"2", 4) == -math.inf
    
def test_minmax_maximizer_tie():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.board = [
        ['1', '2', '1', '2', '1', '2', '?'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert new_game.min_max(new_game.board,"1", 4) == 0


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
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '2', '?', '2', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '2', '?', '2', '2', '?'],
        ['?', '2', '2', '?', '2', '?', '?']]
    assert game.heuristic_score(board) == -6
