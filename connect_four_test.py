import pytest
from connect_four import Board, Game

# Board test cases
def test_board_is_full_with_full_board():
    new_board = Board()
    new_board.board = [["R" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == True

def test_board_is_full_with_not_full_board():
    new_board = Board()
    new_board.board = [["?" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == False

# Game test cases
def test_row_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['R', 'B', 'R', 'B', 'R', 'B', 'R']]
    assert new_game.check_row() == False
    
def test_row_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['B', 'B', 'R', 'R', 'R', 'R', 'B']]
    assert new_game.check_row() == True

def test_column_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', 'B'],
        ['?', '?', '?', '?', '?', 'R', 'B'],
        ['?', '?', '?', '?', '?', 'R', 'B'],
        ['?', '?', '?', '?', '?', 'R', 'B']]
    assert new_game.check_column() == True

def test_column_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', 'R'],
        ['?', '?', '?', '?', '?', '?', 'B'],
        ['?', '?', '?', '?', '?', 'R', 'B'],
        ['?', '?', '?', '?', '?', 'R', 'B']]
    assert new_game.check_column() == False

def test_diagonal_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', 'B'],
        ['?', '?', '?', '?', '?', 'B', 'R'],
        ['?', '?', '?', '?', 'B', 'R', 'B'],
        ['?', '?', '?', 'B', 'R', 'R', 'R']]
    assert new_game.check_diagonals() == True

def test_diagonal_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', 'B', 'R'],
        ['?', '?', '?', '?', 'B', 'R', 'B'],
        ['?', '?', '?', 'B', 'R', 'R', 'R']]
    assert new_game.check_diagonals() == False

def test_other_diagonal_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['B', '?', '?', '?', '?', '?', '?'],
        ['R', 'B', '?', '?', '?', '?', '?'],
        ['B', 'R', 'B', '?', '?', '?', '?'],
        ['R', 'R', 'R', 'B', '?', '?', '?']]
    assert new_game.check_diagonals() == True

@pytest.mark.skip(reason="unfinished test")
def test_get_player_AI():
    game = Game()
    game.input = lambda: 'some input'

    game.get_player_AI()

    assert game.player1 != None and game.player2 != None

