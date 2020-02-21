from copy import deepcopy
from board import Board
from math import sqrt , log, inf
from random import randint
from time import sleep

def monte_carlo_tree_search(current_board, current_player):
    #need to replace this with a better metric for resources left
    num_rollouts = 500
    root = Node(None, board = current_board)
    root.get_children_nodes(current_player)

    while num_rollouts > 0 :
        node_to_expand = traverse(root)
        winner, final_node = rollout(node_to_expand, current_player)
        #print(winner)
        backpropogate_scores(final_node, winner)
        num_rollouts -= 1
    
    return best_move(root)

# Main Methods
def traverse(node):
    current_node = node
    while fully_expanded(current_node):
        current_node = best_ucb(current_node)
    return pick_unvisited(current_node) or current_node

def rollout(node, current_player):
    winner = node.board.provide_winner(node.board)
    tie = node.board.board_is_full()
    turn = current_player
    new_node = node

    while not winner and not tie:
        turn = switch_turns(turn)
        new_node = rollout_policy(new_node, turn)
        winner = new_node.board.provide_winner(new_node.board)
        tie = new_node.board.board_is_full()

    if tie and not winner:
        winner = [["0"]]

    return winner[0][0], new_node

def backpropogate_scores(node, winner):
    if is_root(node):
        node.times_visited += 1
        return
    
    update_stats(node,winner)
    backpropogate_scores(node.parent_node,winner)

### Helper Methods ###
class Node:
    def __init__(self, move, board = Board(), score = 0,times_visited = 0, parent_node = None, turn = None):
        self.score = score
        self.times_visited = times_visited
        self.children = []
        self.board = board
        self.column = move
        self.parent_node = parent_node
        self.turn = turn
    
    def add_child(self,child_node):
        self.children.append(child_node)

    def get_children_nodes(self, player):
        for column in range(7):
            if self.board.does_column_have_space(column):
                new_board = deepcopy(self.board)
                new_board.place(column,player)
                new_node = Node(column, board = new_board, parent_node = self, turn = player)
                self.add_child(new_node)

    def is_leaf(self):
        return not self.children 

# Tree Helpers
def best_move(root):
    best_column = None
    most_visited = -inf
    for node in root.children:
        if node.times_visited > most_visited:
            most_visited = node.times_visited
            best_column = node.column
    return best_column

# Traverse Helpers
def ucb_scoring(node):
    score = (node.score/node.times_visited) + sqrt(2) * sqrt(log(node.parent_node.times_visited)/node.times_visited)
    return score

def best_ucb(node):
    max_score = -inf
    best_node = None
    for child in node.children:
        score = ucb_scoring(child)
        if score > max_score:
            max_score = score
            best_node = child
    return best_node

def fully_expanded(node):
    if node.children == []:
        return False
    
    for child in node.children:
        if child.times_visited == 0:
            return False

    return True

def pick_unvisited(node):
    if node.children == []:
        return None
    possible_children = []
    for child in node.children:
        if child.times_visited == 0:
            possible_children.append(child)
    index = randint(0, len(possible_children)-1)
    return possible_children[index]

# Rollout Helpers
def switch_turns(current_player):
    if current_player == "1":
        return "2"
    else:
        return "1"

def rollout_policy(node, turn):
    node.get_children_nodes(turn)
    index = randint(0,len(node.children)-1)
    return node.children[index]

# Backpropogate Helpers

def is_root(node):
    return node.parent_node == None

def update_stats(node,winner):
    if node.turn == winner:
        node.score += 1

    if winner == "0":
        node.score += 0.1

    node.times_visited += 1