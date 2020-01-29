import pytest
from connect_four import Board, Game, check_four_consecutive,check_potential_win

# Board utility test cases
def test_get_all_moves():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '?']]
    all_moves_board_objects = new_game.board.get_all_moves("2")
    list_of_just_boards = []
    for board_object in all_moves_board_objects:
        list_of_just_boards.append(board_object.board)
    assert list_of_just_boards == [[
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['2', '?', '?', '1', '?', '?', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '2', '?', '1', '?', '?', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '2', '1', '?', '?', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '2', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '2', '?']],
        [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '2']]]

# Board checker test cases
def test_board_is_full_with_full_board():
    new_board = Board()
    new_board.board = [["1" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == True

def test_board_is_full_with_not_full_board():
    new_board = Board()
    new_board.board = [["?" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == False

# Game Win checking test cases
def test_row_not_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert board.check_row(check_four_consecutive) == None

def test_row_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['1', '1', '2', '2', '2', '2', '1']]
    assert board.check_row(check_four_consecutive) == [["2"]]

def test_column_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1']]
    assert board.check_column(check_four_consecutive) == [["1"]]

def test_column_not_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1']]
    assert board.check_column(check_four_consecutive) == None

def test_diagonal_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.check_diagonals(check_four_consecutive) == [["1"]]

def test_diagonal_win_other_loop():
    board = Board()
    board.board = [
        ['?', '?', '?', '1', '?', '2', '1'],
        ['?', '?', '1', '?', '2', '1', '?'],
        ['?', '1', '?', '?', '?', '?', '1'],
        ['1', '?', '2', '1', '?', '?', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '?', '2', '2', '2']]
    assert board.check_diagonals(check_four_consecutive) == [["1"]]

def test_other_diagonal_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '1', '?', '?', '?'],
        ['?', '?', '?', '?', '1', '?', '?'],
        ['1', '?', '?', '?', '?', '1', '?'],
        ['2', '?', '?', '?', '?', '?', '1'],
        ['1', '2', '1', '?', '?', '?', '?'],
        ['2', '2', '2', '1', '?', '?', '?']]
    assert board.check_diagonals(check_four_consecutive) == [["1"]]

def test_other_diagonal_win_other_loop():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['1', '?', '?', '?', '?', '?', '?'],
        ['2', '1', '?', '?', '?', '?', '?'],
        ['1', '2', '1', '?', '?', '?', '?'],
        ['2', '2', '2', '1', '?', '?', '?']]
    assert board.check_diagonals(check_four_consecutive) == [["1"]]

def test_diagonal_not_win():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.check_diagonals(check_four_consecutive) == None

def test_provide_winner():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.provide_winner() == [["1"]]

def test_provide_winner_tie():
    board = Board()
    board.board = [
        ['1', '2', '1', '2', '1', '2', '1'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert board.provide_winner() == None

def test_provide_winner_no_winner():
    board = Board()
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.provide_winner() == None

def test_check_potential_win():
    assert check_potential_win(["1","2","2","?","2","2","1"])==["2","2"]

# Game AI Test Cases
@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board, "1") == 1

@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board, "1") == -1

@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board, "1") == 0

@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board,"1") == 1
    
@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board,"2") == -1
    
@pytest.mark.skip(reason="no way of currently testing this")
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
    assert new_game.min_max(new_game.board,"1") == 0

# Game AI Helpers
def test_get_opposite_symbol():
    game = Game()
    assert game.get_opposite_symbol("1") == "2"
    assert game.get_opposite_symbol("2") == "1"
