from copy import deepcopy
from board import Board
from math import sqrt , log, inf
from random import randint
from time import sleep

def monte_carlo_tree_search(current_board, current_player):
    #need to replace this with a better metric for resources left
    num_rollouts = 100
    root = Node(None, board = current_board, person_who_just_played= switch_turns(current_player))
    root.get_children_nodes()

    while num_rollouts > 0 :
        node_to_expand = traverse(root)
        winner = rollout(node_to_expand, current_player)
        backpropagate_scores(node_to_expand, winner)
        num_rollouts -= 1

    return best_move(root)

# Main Methods
def traverse(node):
    current_node = node
    while fully_expanded(current_node):
        current_node = best_ucb(current_node)
    return pick_unvisited(current_node) or current_node

def rollout(node, current_player):
    if node.times_visited == 0:
        node.get_children_nodes()

    winner = rollout_policy(node)

    return winner[0][0]

def backpropagate_scores(node, winner):
    if is_root(node):
        node.times_visited += 1
        return
    
    update_stats(node,winner)
    backpropagate_scores(node.parent_node,winner)

### Helper Methods ###
class Node:
    def __init__(self, move, board = Board(), score = 0,times_visited = 0, parent_node = None, person_who_just_played = None):
        self.score = score
        self.times_visited = times_visited
        self.children = None
        self.board = board
        self.column = move
        self.parent_node = parent_node
        self.person_who_just_played = person_who_just_played
    
    def add_child(self,child_node):
        self.children.append(child_node)

    def get_children_nodes(self):
        self.children = []

        if self.board.provide_winner() != [None]:
            return

        next_player = switch_turns(self.person_who_just_played)
        for column in range(7):
            if self.board.does_column_have_space(column):
                new_board = deepcopy(self.board)
                new_board.place(column,next_player)
                new_node = Node(column, board = new_board, parent_node = self, person_who_just_played = next_player)
                self.add_child(new_node)

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

def rollout_policy(node):
    playout_board = node.board
    winner = playout_board.provide_winner()

    person_who_just_played = node.person_who_just_played
    while winner == [None]:
        person_who_just_played = switch_turns(person_who_just_played)
        while True:
            column = get_random_column()
            if playout_board.does_column_have_space(column):
                break
        playout_board.place(column, person_who_just_played)
        winner = playout_board.provide_winner()

    return winner

def get_random_column():
    column = randint(0,6)
    return column

# Backpropagate Helpers

def is_root(node):
    return node.parent_node == None

def update_stats(node,winner):
    if node.person_who_just_played == winner:
        node.score += 1

    elif winner == "0":
        node.score += 0

    else:
        node.score += -1

    node.times_visited += 1