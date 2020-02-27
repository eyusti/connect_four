#!/usr/bin/env python3
from random import randint
import math
from board import Board, check_potential_win, check_potential_win_two, check_potential_win_two_weighted, final_heuristic
from monte_carlo import monte_carlo_tree_search
       
class Game:
    def __init__(self):
        #Player can be string of name of AI
        self.player1 = None
        self.p1_color = "1"
        self.player2 = None
        self.p2_color = "2"
        self.current_turn = 1
        self.current_color = None
        self.board = Board()
        self.max = 1000000000
        self.min = -1000000000
        
        #These are flags
        self.do_alpha_beta_pruning = True
        self.discount = .99
        self.set_heuristic_score = None

# Game Setup
    def get_player_AI(self):
        #this is out of date 
        print("Welcome to Connect Four! What AIs would you like to play against each other?")
        while True:
            try: 
                self.player1 = input("Which AI would you like for player 1? (RNG / MinMax2 / MinMax3) ").lower()
                while self.player1 not in ["rng","minmax2","minmax3"]:
                    self.player1 = input("Sorry, that isn't an AI we have. Which AI would you like for player 1? (RNG / MinMax2 / MinMax3) ").lower()     
            except ValueError:
                print("I'm sorry Dave, I'm afraid I can't do that")
                continue
            else:
                break
        while True:
            try: 
                self.player2 = input("Which AI would you like for player 2? (RNG / MinMax2 / MinMax3) ").lower()
                while self.player2 not in ["rng","minmax","minmax3"]:
                    self.player2 = input("Sorry, that isn't an AI we have. Which AI would you like for player 2? (RNG / MinMax2 / MinMax3) ").lower()     
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
                        #self.board.print_board()
                        break
            
            if current_AI == "human":
                #checks permutations of three
                column = int(input("Column: "))
                self.board.place(column, self.current_color)

            if current_AI == "minmax3":
                #checks permutations of three
                self.set_heuristic_score = check_potential_win
                _score, column = self.min_max(self.board,self.current_color,3, -math.inf, math.inf)
                self.board.place(column, self.current_color)
                #self.board.print_board()
            
            if current_AI == "minmax2":
                #checks permutations of two and three
                self.set_heuristic_score = check_potential_win_two
                _score, column = self.min_max(self.board,self.current_color,3, -math.inf, math.inf)
                self.board.place(column, self.current_color)
                #self.board.print_board()
            
            if current_AI == "minmax2_w":
                #checks permutations of two and three with three more heavily
                self.set_heuristic_score = check_potential_win_two_weighted
                _score, column = self.min_max(self.board,self.current_color,2, -math.inf, math.inf)
                self.board.place(column, self.current_color)
                #self.board.print_board()
            
            if current_AI == "minmax2_w_f":
                #checks permutations of two and three with three more heavily, makes first move in middle
                if self.board.board[5][3] == "?":
                    self.board.place(3, self.current_color)
                    #self.board.print_board()
                else:
                    self.set_heuristic_score = check_potential_win_two_weighted
                    _score, column = self.min_max(self.board,self.current_color,2, -math.inf, math.inf)
                    self.board.place(column, self.current_color)
                    #self.board.print_board()

            if current_AI == "final_heuristic":
                #checks permutations of one, two, three, and four, makes first move in middle
                if self.board.board[5][3] == "?":
                    self.board.place(3, self.current_color)
                    self.board.print_board()
                else:
                    self.set_heuristic_score = final_heuristic
                    _score, column = self.min_max(self.board,self.current_color, 5, -math.inf, math.inf)
                    self.board.place(column, self.current_color)
                    self.board.print_board()

            if current_AI == "montecarlo":
                column = monte_carlo_tree_search(self.board, self.current_color)
                self.board.place(column, self.current_color)
                self.board.print_board()

            winner = self.board.provide_winner()

            if winner == [["0"]]:
                #print("The game is a tie")
                return "tie"

            if winner != [None]:
                print("The game has been won by: Player " + winner[0][0])
                return winner[0][0]
            
            self.switch_current_player()
            
# AI Solutions
    def rng_move(self):
        column = randint(0,6)
        return column

    def min_max(self, board, player, depth, alpha, beta):
        winner = board.provide_winner()
        if winner == [[self.current_color]]:
            return self.max, None
        if winner == [["0"]]:
            return 0, None
        if winner != [None]:
            return self.min, None   
        if depth == 0:
            return self.heuristic_score(board) , None
            
        all_move_boards = board.get_all_moves(player)

        if player is self.current_color:
            maxEval = self.min
            best_column = all_move_boards[0][1]
            for move_board, column in all_move_boards: 
                eval, _column = self.min_max(move_board, self.get_opposite_symbol(player), depth - 1, alpha, beta)
                eval *= .99
                if eval > maxEval:
                    best_column = column
                    maxEval = eval
                alpha = max(alpha,maxEval)
                if self.do_alpha_beta_pruning and alpha >= beta:
                    break
            return maxEval , best_column

        else:
            minEval = self.max
            best_column = all_move_boards[0][1]
            for move_board, column in all_move_boards:
                eval, _column =  self.min_max(move_board, self.get_opposite_symbol(player), depth - 1, alpha, beta)
                eval *= .99
                if eval < minEval:
                    best_column = column
                    minEval = eval
                beta = min(beta, minEval)
                if self.do_alpha_beta_pruning and alpha >= beta:
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
        temp_row = board.check_row(self.set_heuristic_score)
        temp_column = board.check_column(self.set_heuristic_score)
        temp_diagonal = board.check_diagonals(self.set_heuristic_score)

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

def main():
    new_game = Game()
    new_game.get_player_AI()
    new_game.play_game()

if __name__ == "__main__":
    main()

