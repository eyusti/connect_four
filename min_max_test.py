import pytest
import math
from connect_four import Game 
from board import Board, check_four_consecutive, check_potential_win, check_potential_win_two_weighted

def test_minmax_winning_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.last_placed_column =3
    new_game.board.last_placed_row = 2
    new_game.board.last_placed_player = "1"
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?']]
    assert new_game.min_max(new_game.board, "1", 4, -math.inf, math.inf) == (new_game.max, None)

def test_minmax_losing_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.last_placed_column = 4
    new_game.board.last_placed_row = 2
    new_game.board.last_placed_player = "2"
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?'],
        ['?', '?', '1', '1', '2', '?', '?']]
    assert new_game.min_max(new_game.board, "1", 4, -math.inf, math.inf) == (new_game.min, None)

def test_minmax_tied_board_scoring():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.last_placed_column = 6
    new_game.board.last_placed_row = 0
    new_game.board.last_placed_player = "1"
    new_game.board.board = [
        ['1', '2', '1', '2', '1', '2', '1'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert new_game.min_max(new_game.board, "1", 4, -math.inf, math.inf) == (0, None)

def test_minmax_maximizer_win():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.last_placed_column = 5
    new_game.board.last_placed_row = 0
    new_game.board.last_placed_player = "2"
    new_game.board.board = [
        ['1', '1', '1', '2', '2', '2', '?'],
        ['2', '2', '2', '1', '1', '1', '?'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2']]
    _score, column = new_game.min_max(new_game.board,"1", 4, -math.inf, math.inf)
    assert  column == 6
    
def test_minmax_maximizer_lose():
    new_game = Game()
    new_game.current_color = "1"
    new_game.board.last_placed_column = 6
    new_game.board.last_placed_row = 2
    new_game.board.last_placed_player = "1"
    new_game.board.board = [
        ['1', '1', '1', '2', '?', '2', '?'],
        ['2', '2', '2', '1', '?', '1', '?'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2'],
        ['1', '1', '1', '2', '2', '2', '1'],
        ['2', '2', '2', '1', '1', '1', '2']]
    
    _score, column = new_game.min_max(new_game.board,"2", 4, -math.inf, math.inf)
    assert column == 4
    
def test_minmax_maximizer_tie():
    new_game = Game()
    new_game.board.last_placed_column = 4
    new_game.board.last_placed_row = 0
    new_game.board.last_placed_player = "2"
    new_game.current_color = "1"
    new_game.board.board = [
        ['1', '2', '1', '2', '1', '2', '?'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert new_game.min_max(new_game.board,"1", 4, -math.inf, math.inf) == (0,6)

def test_minmax_just_returning_first_column_checked():
    new_game = Game()
    new_game.board.last_placed_column = 3
    new_game.board.last_placed_row = 0
    new_game.board.last_placed_player = "2"
    new_game.current_color = "1"
    new_game.board.board = [
        ['?', '?', '1', '2', '1', '2', '1'],
        ['1', '?', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    _score, column = new_game.min_max(new_game.board,"1", 8, -math.inf, math.inf)
    assert  column == 1

def test_minmax_just_returning_last_column_checked():
    new_game = Game()
    new_game.board.last_placed_column = 3
    new_game.board.last_placed_row = 0
    new_game.board.last_placed_player = "2"
    new_game.current_color = "1"
    new_game.board.board = [
        ['?', '?', '1', '2', '1', '2', '?'],
        ['1', '?', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    
    _score, column = new_game.min_max(new_game.board,"1", 8, -math.inf, math.inf)
    assert  column == 1

def test_minmax_diminishing_future_returns():
    new_game = Game()
    new_game.board.last_placed_column = 2
    new_game.board.last_placed_row = 1
    new_game.board.last_placed_player = "1"
    new_game.current_color = "2"
    new_game.set_heuristic_score = check_potential_win
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['2', '?', '1', '?', '?', '?', '?'],
        ['1', '?', '1', '?', '?', '2', '?'],
        ['2', '?', '2', '1', '?', '1', '?'],
        ['2', '?', '1', '2', '?', '1', '?'],
        ['2', '?', '2', '1', '1', '1', '2']]
    _score, column = new_game.min_max(new_game.board,"2", 5, -math.inf, math.inf)
    assert column == 4

@pytest.mark.skip(reason="was for debugging, no need for regular run")
def test_minmax_alpha_beta_breaking_min_max():
    alpha_beta = Game()
    min_max = Game()
    alpha_beta.current_color = "1"
    min_max.current_color = "1"
    alpha_beta.do_alpha_beta_pruning = True
    min_max.do_alpha_beta_pruning = False
    alpha_beta.set_heuristic_score = check_potential_win
    min_max.set_heuristic_score = check_potential_win
    alpha_beta.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['1', '?', '1', '1', '?', '2', '2']]
    min_max.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['1', '?', '1', '1', '?', '2', '2']]
    _score_1, column_1 = alpha_beta.min_max(alpha_beta.board,"1", 5, -math.inf, math.inf) 
    _score_2, column_2 = min_max.min_max(min_max.board,"1", 5, -math.inf, math.inf) 

    assert column_1 == column_2
    assert column_1 == 1
    assert column_2 == 1
@pytest.mark.skip(reason="was for debugging, no need for regular run")
def test_minmax_alpha_beta_breaking_min_max_block():
    alpha_beta = Game()
    min_max = Game()
    alpha_beta.current_color = "2"
    min_max.current_color = "2"
    alpha_beta.do_alpha_beta_pruning = True
    min_max.do_alpha_beta_pruning = False
    alpha_beta.set_heuristic_score = check_potential_win
    min_max.set_heuristic_score = check_potential_win
    alpha_beta.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['1', '?', '1', '1', '?', '2', '2']]
    min_max.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['1', '?', '1', '1', '?', '2', '2']]
    _score_1, column_1 = alpha_beta.min_max(alpha_beta.board,"2", 5, -math.inf, math.inf) 
    _score_2, column_2 = min_max.min_max(min_max.board,"2", 5, -math.inf, math.inf) 

    assert column_1 == column_2
    assert column_1 == 1
    assert column_2 == 1