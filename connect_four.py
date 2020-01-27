#!/usr/bin/env python3
from pprint import pprint
from random import randint

class Board:
    def __init__(self):
        self.board = [["?" for column in range(7)]for row in range(6)]

    def print_board(self):
        pprint(self.board)

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

    def place(self, column, player_color):
        for row in range(5,-1,-1):
            if self.board[row][column] == "?":
                self.board[row][column] = player_color
                return


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
            return
        if self.current_turn == 2:
            self.current_turn = 1
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
                winner = self.provide_winner()
                if winner:
                    print("The game has been won by: " + winner)
                    return 

                self.switch_current_player()
                
                """if current_AI == "Negamax":
                    column, score = Negamax()
                    place(column, self.current_color)"""
# AI Solutions
    def rng_move(self):
        column = randint(0,6)
        return column

    def min_max(self, board, player):
        winner = self.provide_winner()
        if winner == player:
            return 1
        elif not winner and self.board.board_is_full():
            return 0
        else:
            return -1
        """
        if game is won return score

        if player is maximizing player:
            maxEval = + infinity
            for move_board in all_move_boards: 
                eval = min_max(move_board)
                maxEval = max(maxEval, eval)
                return maxEval
        
        if player is minimizing player:
            minEval = - infinity
            for move_board in all_move_board:
                eval =  min_max(move_board)
                minEval = min(minEval,eval)
                return minEval

        
        """

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
            symb_winner = self.check_four_consecutive(self.board.board[row])
            if symb_winner:
                return symb_winner
        return None       

    def check_column(self):
        column_list = []
        for column in range(7):
            for row in range(6):
                column_list.append(self.board.board[row][column])
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
                diagonal_list.append(self.board.board[r_index][c_index])
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
                diagonal_list.append(self.board.board[r_index][c_index])
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
                diagonal_list.append(self.board.board[r_index][c_index])
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
                diagonal_list.append(self.board.board[r_index][c_index])
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

def main():
    new_game = Game()
    new_game.get_player_AI()
    new_game.play_game()

if __name__ == "__main__":
    main()
