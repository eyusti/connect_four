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
                all_moves.append(new_board)
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
    def check_four_consecutive(self,any_list):
        visited_list = []
        visited_list.append(any_list[0])
        for item in any_list[1:]:
            if item in visited_list and item != "?":
                visited_list.append(item)
                if len(visited_list) >= 4:
                    return visited_list[0]
            if item not in visited_list:
                visited_list = []
                visited_list.append(item)
        return None

    def check_row(self):
        for row in range(6):
            symb_winner = self.check_four_consecutive(self.board[row])
            if symb_winner:
                return symb_winner
        return None       

    def check_column(self):
        for column in range(7):
            column_list = []
            for row in range(6):
                column_list.append(self.board[row][column])
            symb_winner = self.check_four_consecutive(column_list)
            if symb_winner:
                return symb_winner
        return None

    def check_diagonals(self):
        diagonal_list = []
        c_index = 0
        r_index = 0
        routine_index = 0
        
        #test_other_diagonal_win
        while routine_index < 4:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
                c_index += 1
                r_index += 1
            symb_winner = self.check_four_consecutive(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = routine_index
            r_index = 0
            if symb_winner:
                return symb_winner

        c_index = 0
        r_index = 0
        routine_index = 0
        
        #test_other_diagonal_win_other_loop
        while routine_index < 3:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
                c_index += 1
                r_index += 1
            symb_winner = self.check_four_consecutive(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = 0
            r_index = routine_index
            if symb_winner:
                return symb_winner

        c_index = 6
        r_index = 0
        routine_index = 6
        
        #test_diagonal_win_other_loop
        while routine_index > 2:
            while c_index >= 0 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
                c_index -= 1
                r_index += 1
            symb_winner = self.check_four_consecutive(diagonal_list)
            diagonal_list = []
            routine_index -= 1
            c_index = routine_index
            r_index = 0
            if symb_winner:
                return symb_winner
        
        c_index = 6
        r_index = 0
        routine_index = 0
        
        #test_diagonal_win
        while routine_index < 3:
            while c_index > 0 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
                c_index -= 1
                r_index += 1
            symb_winner = self.check_four_consecutive(diagonal_list)
            diagonal_list = []
            routine_index += 1
            c_index = 6
            r_index = routine_index
            if symb_winner:
                return symb_winner

        return None
    
    def provide_winner(self):
        symb_winner = self.check_row() or self.check_column() or self.check_diagonals()
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
                while self.player2 not in ["rng","MinMax"]:
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
            # refactor this with winner method once created
            winner = self.board.provide_winner()

            if winner:
                print("The game has been won by: Player " + winner)
                return 

            self.switch_current_player()
            
            """if current_AI == "minmax":
                score, column = min_max(,self.current_color)
                place(column, self.current_color)"""

# AI Solutions
    def rng_move(self):
        column = randint(0,6)
        return column

    def min_max(self, board, player):
        winner = board.provide_winner()
        if winner == self.current_color:
            return 1
        if winner:
            return -1
        if not winner and board.board_is_full():
            return 0
            
        all_move_boards = board.get_all_moves(player)

        if player is self.current_color:
            maxEval = -math.inf
            for move_board in all_move_boards: 
                eval = self.min_max(move_board, self.get_opposite_symbol(player))
                maxEval = max(maxEval, eval)
                return maxEval

        else:
            minEval = math.inf
            for move_board in all_move_boards:
                eval =  self.min_max(move_board, self.get_opposite_symbol(player))
                minEval = min(minEval,eval)
                return minEval

# AI Helper Methods
    def get_opposite_symbol(self, player):
        if player == "1":
            return "2"
        else:
            return "1"

def main():
    new_game = Game()
    new_game.get_player_AI()
    new_game.play_game()

if __name__ == "__main__":
    main()

