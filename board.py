from copy import deepcopy
from pprint import pprint

class Board:
    def __init__(self):
        self.board = [["?" for column in range(7)]for row in range(6)]
        self.last_placed_row = None
        self.last_placed_column = None
        self.last_placed_player = None

# Utility
    def print_board(self):
        pprint(self.board)

    def place(self, column, player_color):
        self.last_placed_column = column
        self.last_placed_player = player_color
        for row in range(5,-1,-1):
            if self.board[row][column] == "?":
                self.board[row][column] = player_color
                self.last_placed_row = row
                return

    def get_all_moves(self, player_color):
        all_moves = []
        for column in range(7):
            if self.does_column_have_space(column):
                new_board = deepcopy(self)
                new_board.place(column,player_color)
                all_moves.append((new_board,column))
        return all_moves

    def board_is_full(self):
        for column in range(7):
            if self.board[0][column] == "?":
                return False
        return True
    
    def does_column_have_space(self, column):
        return self.board[0][column] == "?"

# Heuristic Checkers
    def check_row(self,function):
        list_symb_winner_list = []
        for row in range(6):
            symb_winner_list = function(self.board[row])
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)
        if list_symb_winner_list:
            return list_symb_winner_list
        return None       

    def check_column(self, function):
        list_symb_winner_list = []
        for column in range(7):
            column_list = []
            for row in range(6):
                column_list.append(self.board[row][column])
            symb_winner_list = function(column_list)
            if symb_winner_list:
                list_symb_winner_list.append(symb_winner_list)
        if list_symb_winner_list:
            return list_symb_winner_list
        return None

    def check_diagonals(self, function):
        diagonal_list = []
        c_index = 0
        r_index = 0
        routine_index = 0
        list_symb_winner_list = []

        #test_other_diagonal_win
        while routine_index < 4:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
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
        r_index = 1
        routine_index = 0
        
        #test_other_diagonal_win_other_loop
        while routine_index < 3:
            while c_index < 7 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
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
                diagonal_list.append(self.board[r_index][c_index])
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
        r_index = 1
        routine_index = 0
        
        #test_diagonal_win
        while routine_index < 3:
            while c_index > 0 and r_index < 6:
                diagonal_list.append(self.board[r_index][c_index])
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
    
    def provide_winner(self):
        if self.last_placed_player == None:
            return [None]

        symb_winner_tie = None
        symb_winner_column = None
        symb_winner_diagonal_1 = None
        symb_winner_diagonal_2 = None

        #check tie
        if self.board_is_full():
            symb_winner_tie = ["0"]
        #check row
        symb_winner_row = check_four_consecutive(self.board[self.last_placed_row])
        #check column
        if self.last_placed_row <= 2:
            if self.board[self.last_placed_row][self.last_placed_column] == self.last_placed_player and self.board[self.last_placed_row + 1][self.last_placed_column] == self.last_placed_player and self.board[self.last_placed_row+2][self.last_placed_column] == self.last_placed_player and self.board[self.last_placed_row+3][self.last_placed_column] == self.last_placed_player:
                symb_winner_column = [self.last_placed_player]
        #check diagonal
        diagonal_1 = []

        for index in range(-3,3):
            row = self.last_placed_row + index
            column = self.last_placed_column + index
            if row >= 0 and row<=5 and column>=0 and column<=6:
                diagonal_1.append(self.board[row][column])

        symb_winner_diagonal_1 = check_four_consecutive(diagonal_1)

        diagonal_2 = []
        for index in range(-3,3):
            row = self.last_placed_row + index
            column = self.last_placed_column + (index * -1)
            if row >= 0 and row<=5 and column>=0 and column<=6:
                diagonal_2.append(self.board[row][column])
        
        symb_winner_diagonal_2 = check_four_consecutive(diagonal_2)

        symb_winner = symb_winner_tie or symb_winner_row or symb_winner_column or symb_winner_diagonal_1 or symb_winner_diagonal_2
        
        return [symb_winner]

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
        if temp in [["1","1","?","?"],["1","?","1","?"],["1","?","?","1"],["?","1","1","?"],["?","1","?","1"],["?","?","1","1"],["2","2","?","?"],["2","?","2","?"],["2","?","?","2"],["?","2","2","?"],["?","2","?","2"],["?","?","2","2"],["?","1","1","1"],["1","?","1","1"],["1","1","?","1"],["1","1","1","?"],["?","2","2","2"],["2","?","2","2"],["2","2","?","2"],["2","2","2","?"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
        c_index += 1
    return list_of_potential_winning_symbols

def check_potential_win_two_weighted(any_list):
    c_index = 0
    list_of_potential_winning_symbols = []
    while c_index < len(any_list) - 3:
        temp = any_list[c_index: c_index + 4]
        if temp in [["1","1","?","?"],["1","?","1","?"],["1","?","?","1"],["?","1","1","?"],["?","1","?","1"],["?","?","1","1"],["2","2","?","?"],["2","?","2","?"],["2","?","?","2"],["?","2","2","?"],["?","2","?","2"],["?","?","2","2"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
        if temp in [["?","1","1","1"],["1","?","1","1"],["1","1","?","1"],["1","1","1","?"],["?","2","2","2"],["2","?","2","2"],["2","2","?","2"],["2","2","2","?"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
        c_index += 1
    return list_of_potential_winning_symbols

def final_heuristic(any_list):
    c_index = 0
    list_of_potential_winning_symbols = []
    while c_index < len(any_list) - 3:
        temp = any_list[c_index: c_index + 4]
        if temp in [["1","?","?","?"],["?","1","?","?"],["?","?","1","?"],["?","?","?","1"],["2","?","?","?"],["?","2","?","?"],["?","?","2","?"],["?","?","?","2"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
        if temp in [["1","1","?","?"],["1","?","1","?"],["1","?","?","1"],["?","1","1","?"],["?","1","?","1"],["?","?","1","1"],["2","2","?","?"],["2","?","2","?"],["2","?","?","2"],["?","2","2","?"],["?","2","?","2"],["?","?","2","2"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
        if temp in [["?","1","1","1"],["1","?","1","1"],["1","1","?","1"],["1","1","1","?"],["?","2","2","2"],["2","?","2","2"],["2","2","?","2"],["2","2","2","?"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
        if temp in [["1","1","1","1"],["2","2","2","2"]]:
            if "1" in temp:
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
                list_of_potential_winning_symbols.append("1")
            if "2" in temp:
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
                list_of_potential_winning_symbols.append("2")
        c_index += 1
    return list_of_potential_winning_symbols