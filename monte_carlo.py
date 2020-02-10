from copy import deepcopy
from connect_four import Board
from math import sqrt , log, inf

def monte_carlo_tree_search(root, current_player):
    num_rollouts = 1000
    best_move = None

    while num_rollouts > 0 :
        node_to_expand = traverse(root)
        score = rollout(node_to_expand)
        backpropogate_scores(node_to_expand, score)
    
    return best_move(root)

# Main Methods
def traverse(root):
    current_node = root
    temp_node = None
    while not current_node.is_leaf():
        max_score = -inf
        for child in current_node.children:
            score = ucb_scoring(child)
            if score > max_score:
                max_score = score
                temp_node = child
        current_node = temp_node
    return current_node

def rollout(node):
    score = None
    return score

def backpropogate_scores(node, score):
    pass

# Helper Methods
class Node:
    def __init__(self, move, board = Board(), score = 0,times_visited = 0, parent_node = None):
        self.score = score
        self.times_visited = times_visited
        self.children = []
        self.board = board
        self.move_column = move
        self.parent_node = parent_node
    
    def add_child(self,child_node):
        self.children.append(child_node)

    def get_children_nodes(self, player):
        for column in range(7):
            if self.board.does_column_have_space(column):
                new_board = deepcopy(self.board)
                new_board.place(column,player)
                new_node = Node(new_board,column)
                self.add_child(new_node)

    def is_leaf(self):
        return not self.children 

def best_move(root):
    best_column = None
    most_visited = -inf
    for node in root.children:
        if node.times_visited > most_visited:
            most_visited = node.times_visited
            best_column = node.move_column
    return best_column

def ucb_scoring(node):
    score = (node.score/node.times_visited) + 2 * sqrt(log(node.parent_node.times_visited)/node.times_visited)
    return score