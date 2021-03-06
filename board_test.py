import pytest
import math
from connect_four import Game
from board import Board, check_four_consecutive, check_potential_win

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
    list_of_just_boards_tuple = []
    for board_move_tuple in all_moves_board_objects:
        board = board_move_tuple[0]
        column = board_move_tuple[1]
        actual_board = board.board
        list_of_just_boards_tuple.append((actual_board,column))
    assert  list_of_just_boards_tuple == [([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['2', '?', '?', '1', '?', '?', '?']],0),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '2', '?', '1', '?', '?', '?']],1),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '2', '1', '?', '?', '?']],2),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '2', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '?']],3),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '2', '?', '?']],4),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '2', '?']],5),
        ([
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '1', '?', '?', '2']],6)]

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
def test_provide_winner_diagonal():
    board = Board()
    board.last_placed_row = 3
    board.last_placed_column = 5
    board.last_placed_player = "1"
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '1'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.provide_winner() == [["1"]]
def test_provide_winner_o_diagonal():
    board = Board()
    board.last_placed_row = 4
    board.last_placed_column = 2
    board.last_placed_player = "1"
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['1', '?', '?', '?', '?', '?', '?'],
        ['?', '1', '?', '?', '?', '?', '2'],
        ['?', '?', '1', '?', '?', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.provide_winner() == [["1"]]

def test_provide_winner_column():
    board = Board()
    board.last_placed_row = 2
    board.last_placed_column = 5
    board.last_placed_player = "1"
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '?', '1', '1'],
        ['?', '?', '?', '?', '2', '1', '2']]
    assert board.provide_winner() == [["1"]]

def test_provide_winner_row():
    board = Board()
    board.last_placed_row = 5
    board.last_placed_column = 2
    board.last_placed_player = "1"
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '2'],
        ['?', '?', '?', '?', '?', '2', '1'],
        ['1', '1', '1', '1', '2', '2', '2']]
    assert board.provide_winner() == [["1"]]

def test_provide_winner_tie():
    board = Board()
    board.last_placed_row = 0
    board.last_placed_column = 6
    board.last_placed_player = "1"
    board.board = [
        ['1', '2', '1', '2', '1', '2', '1'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['1', '2', '1', '1', '1', '2', '1'],
        ['2', '1', '2', '2', '2', '1', '2'],
        ['2', '1', '2', '1', '2', '1', '2']]
    assert board.provide_winner() == [["0"]]

def test_provide_winner_no_winner():
    board = Board()
    board.last_placed_row = 5
    board.last_placed_column = 3
    board.last_placed_player = "1"
    board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '1', '2'],
        ['?', '?', '?', '?', '1', '2', '1'],
        ['?', '?', '?', '1', '2', '2', '2']]
    assert board.provide_winner() == [None]
