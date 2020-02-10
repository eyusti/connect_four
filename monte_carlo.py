from copy import deepcopy
from connect_four import Board
from math import sqrt , log, inf
from random import randint

def monte_carlo_tree_search(current_board, current_player):
    #need to replace this with a better metric for resources left
    num_rollouts = 1000
    root = Node(None, board = current_board)

    while num_rollouts > 0 :
        node_to_expand = traverse(root)
        score = rollout(node_to_expand)
        backpropogate_scores(node_to_expand, score)
        
        num_rollouts -= 1
    
    return best_move(root)

# Main Methods
def traverse(node):
    while fully_expanded(node):
        node = best_ucb(node)
    return pick_unvisited(node) or node

def rollout(node):
    while not_terminal(node):
        node = rollout_policy(node)
    return result(node)

def backpropogate_scores(node, score):
    pass

### Helper Methods ###
class Node:
    def __init__(self, move, board = Board(), score = 0,times_visited = 0, parent_node = None):
        self.score = score
        self.times_visited = times_visited
        self.children = []
        self.board = board
        self.column = move
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
    score = (node.score/node.times_visited) + 2 * sqrt(log(node.parent_node.times_visited)/node.times_visited)
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
    for child in node.children:
        if child.times_visited == 0:
            return False
    return True

def pick_unvisited(node):
    possible_children = []
    for child in node.children:
        if child.times_visited == 0:
            possible_children.append(child)
    index = randint(0, len(possible_children)-1)
    return possible_children[index]