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
        self.player1 = None
        self.p1_color = "R"
        self.player2 = None
        self.p2_color = "B"
        self.current_turn = 0
        self.board = Board()

    def get_player_AI(self):
        print("Welcome to Connect Four! What AIs would you like to play against each other?")
        while True:
            try: 
                self.player1 = input("Which AI would you like for player 1? (RNG / Negamax) ").lower()
                while self.player1 not in ["rng","negamax"]:
                    self.player1 = input("Sorry, that isn't an AI we have. Which AI would you like for player 1? (RNG / Negamax) ").lower()     
            except ValueError:
                print("I'm sorry Dave, I'm afraid I can't do that")
                continue
            else:
                break
        while True:
            try: 
                self.player2 = input("Which AI would you like for player 2? (RNG / Negamax) ").lower()
                while self.player2 not in ["rng","negamax"]:
                    self.player2 = input("Sorry, that isn't an AI we have. Which AI would you like for player 2? (RNG / Negamax) ").lower()     
            except ValueError:
                print("I'm sorry Dave, I'm afraid I can't do that")
                continue
            else:
                break
    
    def switch_current_player(self):
        if self.current_turn == 0:
            self.current_turn = 1
            return
        if self.current_turn == 1:
            self.current_turn = 0
            return

    def rng_move(self):
        column = randint(0,6)
        return column

    def check_four_consecutive(self,any_list):
        visited_list = []
        visited_list.append(any_list[0])
        for item in any_list[1:]:
            if item in visited_list and item != "?":
                visited_list.append(item)
                if len(visited_list) >= 4:
                    return True
            if item not in visited_list:
                visited_list = []
                visited_list.append(item)
        return False

    def check_row(self):
        for row in range(6):
            if self.check_four_consecutive(self.board.board[row]):
                return True
        return False        

    def check_column(self):
        column_list = []
        for column in range(7):
            for row in range(6):
                column_list.append(self.board.board[row][column])
            is_winner = self.check_four_consecutive(column_list)
            if is_winner:
                return True
        return False

    def check_diagonal(self):
        diagonal_list = []
        c_index = 0
        r_index = 0
        column_routine_index = 0

        while column_routine_index < 7:
            print(column_routine_index)
            while c_index < 7 and r_index < 6:
                print(r_index,c_index)
                diagonal_list.append(self.board.board[r_index][c_index])
                c_index += 1
                r_index += 1
            print(diagonal_list)
            is_winner = self.check_four_consecutive(diagonal_list)
            diagonal_list = []
            column_routine_index += 1
            c_index = column_routine_index
            r_index = 0
            if is_winner:
                return True
        
        return False

    def play_game(self):        
        while not self.board.board_is_full():
            current_AI = None
            current_color = None

            if self.current_turn == 0:
                current_AI = self.player1
                current_color = self.p1_color
            if self.current_turn == 1:
                current_AI = self.player2
                current_color = self.p2_color
            
            if current_AI == "rng":
                while True:
                    column = self.rng_move()
                    if self.board.does_column_have_space(column):
                        self.board.place(column, current_color)
                        break
            
            self.switch_current_player()
            self.board.print_board()

            """if current_AI == "Negamax":
                row, column, score = Negamax()
                place(row, column, current_color)"""

new_game = Game()
new_game.board.board = [
    ['?', '?', '?', '?', '?', '?', '?'],
    ['1', '?', '?', '?', '?', '?', '?'],
    ['?', '1', '?', '?', '?', '?', '?'],
    ['?', '?', '1', '?', '?', '?', '?'],
    ['?', '?', '?', '1', '?', '?', '?'],
    ['?', '?', '?', '?', '1', '?', '?']]
print(new_game.check_diagonal())