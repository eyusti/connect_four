import pytest
from connect_four import Board, Game

# Board test cases
def test_board_is_full_with_full_board():
    new_board = Board()
    new_board.board = [["1" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == True

def test_board_is_full_with_not_full_board():
    new_board = Board()
    new_board.board = [["?" for column in range(7)]for row in range(6)]
    assert new_board.board_is_full() == False

# Win checking test cases
def test_row_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert new_game.check_row() == None
    
def test_row_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['1', '1', '2', '2', '2', '2', '1']]
    assert new_game.check_row() == "2"

def test_column_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1']]
    assert new_game.check_column() == "1"

def test_column_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['?', '?', '?', '?', '?', '2', '1']]
    assert new_game.check_column() == None

def test_diagonal_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert new_game.check_diagonals() == "1"

def test_diagonal_win_other_loop():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '1', '?', '2', '1'],
        ['?', '?', '1', '?', '2', '1', '?'],
        ['?', '1', '?', '?', '?', '?', '1'],
        ['1', '?', '2', '1', '?', '?', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '?', '2', '2', '2']]
    assert new_game.check_diagonals() == "1"

def test_other_diagonal_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '1', '?', '?', '?'],
        ['?', '?', '?', '?', '1', '?', '?'],
        ['1', '?', '?', '?', '?', '1', '?'],
        ['2', '?', '?', '?', '?', '?', '1'],
        ['1', '2', '1', '?', '?', '?', '?'],
        ['2', '2', '2', '1', '?', '?', '?']]
    assert new_game.check_diagonals() == "1"

def test_other_diagonal_win_other_loop():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['1', '?', '?', '?', '?', '?', '?'],
        ['2', '1', '?', '?', '?', '?', '?'],
        ['1', '2', '1', '?', '?', '?', '?'],
        ['2', '2', '2', '1', '?', '?', '?']]
    assert new_game.check_diagonals() == "1"

def test_diagonal_not_win():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert new_game.check_diagonals() == None

def test_provide_winner():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert new_game.provide_winner() == "1"

def test_provide_winner_no_winner():
    new_game = Game()
    new_game.board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert new_game.provide_winner() == None
