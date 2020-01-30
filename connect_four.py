#!/usr/bin/env python3
from pprint import pprint
from random import randint
import math
from copy import deepcopy

class Board:
    def __init__(self):
        self.board = [["?" for column in range(7)]for row in range(6)]

# Utility
    def print_board(self):
        pprint(self.board)

    def place(self, column, player_color):
        for row in range(5,-1,-1):
            if self.board[row][column] == "?":
                self.board[row][column] = player_color
                return

    def get_all_moves(self, player_color):
        all_moves = []
        for column in range(7):
            if self.does_column_have_space(column):
                new_board = deepcopy(self)
                new_board.place(column,player_color)
                all_moves.append((new_board,column))
        return all_moves

# Board Checkers
    def board_is_full(self):
        for row in range(6):
            for column in range(7):
                #print(self.board[row][column])
                if self.board[row][column] == "?":
                    return False
        return True
    
    def does_column_have_space(self, column):
        for row in range(6):
            if self.board[row][column] == "?":
                return True
        return False  

# Win Checkers
    def check_row(self,function,board):
        list_symb_winner_list = []
        for row in range(6):
            symb_winner_list = function(board.board[row])
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)
        if list_symb_winner_list:
            return list_symb_winner_list
        return None       

    def check_column(self, function, board):
        list_symb_winner_list = []
        for column in range(7):
            column_list = []
            for row in range(6):
                column_list.append(board.board[row][column])
            symb_winner_list = function(column_list)
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)
        if list_symb_winner_list:
            return list_symb_winner_list
        return None

    def check_diagonals(self, function, board):
        diagonal_list = []
        c_index = 0
        r_index = 0
        routine_index = 0
        list_symb_winner_list = []

        #test_other_diagonal_win
        while routine_index < 4:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(board.board[r_index][c_index])
                c_index += 1
                r_index += 1
            symb_winner_list = function(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = routine_index
            r_index = 0
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)

        c_index = 0
        r_index = 0
        routine_index = 0
        
        #test_other_diagonal_win_other_loop
        while routine_index < 3:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(board.board[r_index][c_index])
                c_index += 1
                r_index += 1
            symb_winner_list = function(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = 0
            r_index = routine_index
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)

        c_index = 6
        r_index = 0
        routine_index = 6
        
        #test_diagonal_win_other_loop
        while routine_index > 2:
            while c_index >= 0 and r_index < 6:
                diagonal_list.append(board.board[r_index][c_index])
                c_index -= 1
                r_index += 1
            symb_winner_list = function(diagonal_list)
            diagonal_list = []
            routine_index -= 1
            c_index = routine_index
            r_index = 0
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)
        
        c_index = 6
        r_index = 0
        routine_index = 0
        
        #test_diagonal_win
        while routine_index < 3:
            while c_index > 0 and r_index < 6:
                diagonal_list.append(board.board[r_index][c_index])
                c_index -= 1
                r_index += 1
            symb_winner_list = function(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = 6
            r_index = routine_index
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)

        if list_symb_winner_list:
            return list_symb_winner_list
            
        return None
    
    def provide_winner(self,board):
        symb_winner = self.check_row(check_four_consecutive,board) or self.check_column(check_four_consecutive,board) or self.check_diagonals(check_four_consecutive,board)
        return symb_winner
       
class Game:
    def __init__(self):
        #can be RNG or MinMax
        self.player1 = None
        self.p1_color = "1"
        self.player2 = None
        self.p2_color = "2"
        self.current_turn = 1
        self.current_color = None
        self.board = Board()

# Game Setup
    def get_player_AI(self):
        print("Welcome to Connect Four! What AIs would you like to play against each other?")
        while True:
            try: 
                self.player1 = input("Which AI would you like for player 1? (RNG / MinMax) ").lower()
                while self.player1 not in ["rng","minmax"]:
                    self.player1 = input("Sorry, that isn't an AI we have. Which AI would you like for player 1? (RNG / MinMax) ").lower()     
            except ValueError:
                print("I'm sorry Dave, I'm afraid I can't do that")
                continue
            else:
                break
        while True:
            try: 
                self.player2 = input("Which AI would you like for player 2? (RNG / MinMax) ").lower()
                while self.player2 not in ["rng","minmax"]:
                    self.player2 = input("Sorry, that isn't an AI we have. Which AI would you like for player 2? (RNG / MinMax) ").lower()     
            except ValueError:
                print("I'm sorry Dave, I'm afraid I can't do that")
                continue
            else:
                break
    
    def switch_current_player(self):
        if self.current_turn == 1:
            self.current_turn = 2
            self.current_color = self.p2_color
            return
        if self.current_turn == 2:
            self.current_turn = 1
            self.current_color = self.p1_color
            return

    def play_game(self):        
        while not self.board.board_is_full():
            current_AI = None

            if self.current_turn == 1:
                current_AI = self.player1
                self.current_color = self.p1_color
            if self.current_turn == 2:
                current_AI = self.player2
                self.current_color = self.p2_color
                
            
            if current_AI == "rng":
                while True:
                    column = self.rng_move()
                    if self.board.does_column_have_space(column):
                        self.board.place(column, self.current_color)
                        self.board.print_board()
                        break

            if current_AI == "minmax":
                _score, column = self.min_max(self.board,self.current_color,5, -math.inf, math.inf)
                self.board.place(column, self.current_color)
                self.board.print_board()

            winner = self.board.provide_winner(self.board)

            if winner:
                print("The game has been won by: Player " + winner[0][0])
                return winner[0][0]
            
            if self.board.board_is_full():
                print("The game is a tie")
                return "tie"

            self.switch_current_player()
            
# AI Solutions
    def rng_move(self):
        column = randint(0,6)
        return column

    def min_max(self, board, player, depth, alpha, beta):
        winner = board.provide_winner(board)
        if winner == [[self.current_color]]:
            return math.inf, None
        if winner:
            return -math.inf, None
        if not winner and board.board_is_full():
            return 0, None
        if depth == 0:
            return self.heuristic_score(board) , None
            
        all_move_boards = board.get_all_moves(player)

        if player is self.current_color:
            maxEval = -math.inf
            best_column = 11
            for move_board, column in all_move_boards: 
                eval, _column = self.min_max(move_board, self.get_opposite_symbol(player), depth - 1, alpha, beta)
                maxEval = max(maxEval, eval)
                alpha = max(alpha,maxEval)
                if maxEval == eval:
                    best_column = column
                if alpha >= beta:
                    break
            return maxEval , best_column

        else:
            minEval = math.inf
            best_column = 11
            for move_board, column in all_move_boards:
                eval, _column =  self.min_max(move_board, self.get_opposite_symbol(player), depth - 1, alpha, beta)
                minEval = min(minEval,eval)
                beta = min(beta, minEval)
                if minEval == eval:
                    best_column = column
                if alpha >= beta:
                    break
            return minEval , best_column

# AI Helper Methods
    def get_opposite_symbol(self, player):
        if player == "1":
            return "2"
        else:
            return "1"

    def heuristic_score(self,board):
        count_1 = 0
        count_2 = 0
        temp_row = board.check_row(check_potential_win,board)
        temp_column = board.check_column(check_potential_win,board)
        temp_diagonal = board.check_diagonals(check_potential_win,board)

        if temp_row:
            for i in range(len(temp_row)):
                count_1 += temp_row[i].count("1")
                count_2 += temp_row[i].count("2")

        if temp_column:
            for i in range(len(temp_column)):
                count_1 += temp_column[i].count("1")
                count_2 += temp_column[i].count("2")
        
        if temp_diagonal:
            for i in range(len(temp_diagonal)):
                count_1 += temp_diagonal[i].count("1")
                count_2 += temp_diagonal[i].count("2")

        if self.current_turn == 1:
            return count_1 - count_2
        
        if self.current_turn == 2:
            return count_2 - count_1

def check_four_consecutive(any_list):
    visited_list = []
    visited_list.append(any_list[0])
    for item in any_list[1:]:
        if item in visited_list and item != "?":
            visited_list.append(item)
            if len(visited_list) >= 4:
                return [visited_list[0]]
        if item not in visited_list:
            visited_list = []
            visited_list.append(item)
    return None

def check_potential_win(any_list):
    c_index = 0
    list_of_potential_winning_symbols = []
    while c_index < len(any_list) - 3:
        temp = any_list[c_index: c_index + 4]
        if temp in [["?","1","1","1"],["1","?","1","1"],["1","1","?","1"],["1","1","1","?"],["?","2","2","2"],["2","?","2","2"],["2","2","?","2"],["2","2","2","?"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
        c_index += 1
    return list_of_potential_winning_symbols

def check_potential_win_two(any_list):
    c_index = 0
    list_of_potential_winning_symbols = []
    while c_index < len(any_list) - 3:
        temp = any_list[c_index: c_index + 4]
        if temp in [["1","1","?","?"],["1","?","1","?"],["1","?","?","1"],["?","1","1","?"],["?","1","?","1"],["?","?","1","1"],["2","2","?","?"],["2","?","2","?"],["2","?","?","2"],["?","2","2","?"],["?","2","?","2"],["?","?","2","2"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
        c_index += 1
    return list_of_potential_winning_symbols

def main():
    new_game = Game()
    new_game.get_player_AI()
    new_game.play_game()

if __name__ == "__main__":
    main()

