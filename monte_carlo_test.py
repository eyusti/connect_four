import pytest
from connect_four import Board
from monte_carlo import Node, ucb_scoring, traverse, best_move, best_ucb, fully_expanded, pick_unvisited, traverse

board = Board()
board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '1', '?', '?', '?', '?', '?']]
board_move = 1
board_node = Node(board_move, board)

# Node Tests
def test_constructor_defaults():
    move = None
    new_node = Node(move)
    assert new_node.score == 0
    assert new_node.times_visited == 0
    assert new_node.board.board == [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?']]

def test_add_node():
    new_node = Node(None)
    new_child_node = Node(None)
    new_node.add_child(new_child_node)
    assert new_child_node in new_node.children  

def test_get_all_children():
    board_node.get_children_nodes("2")
    assert len(board_node.children) == 7

# Main Tree Search
def test_best_move():
    root = Node(None)

    node1 = Node(None, times_visited = 50)
    node1.column = 0

    node2 = Node(None, times_visited = 100)
    node2.column = 1

    node3 = Node(None, times_visited = 734)
    node3.column = 2

    node4 = Node(None, times_visited = 42)
    node4.column = 3

    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)

    assert best_move(root) == 2

# Traverse Helpers
def test_ucb_score():
    root = Node (None,score = 30, times_visited = 2 )
    test_node = Node(None,score = 20, times_visited = 1)
    test_node.parent_node = root
    test_node_two = Node(None, score = 10, times_visited = 1)
    test_node_two.parent_node = root
    root.children.append(test_node)
    root.children.append(test_node_two)
    assert round(ucb_scoring(test_node),2) == 21.67
    assert round(ucb_scoring(test_node_two),2) == 11.67

def test_best_ucb():
    root = Node(None,score = 30, times_visited = 2 )
    test_node = Node(None,score = 20, times_visited = 1)
    test_node.parent_node = root
    test_node_two = Node(None, score = 10, times_visited = 1)
    test_node_two.parent_node = root
    root.children.append(test_node)
    root.children.append(test_node_two)
    assert best_ucb(root) == test_node

def test_fully_expanded_true():
    root = Node(None)
    node1 = Node(None, times_visited = 50)
    node2 = Node(None, times_visited = 100)
    node3 = Node(None, times_visited = 734)
    node4 = Node(None, times_visited = 42)
    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)
    assert fully_expanded(root) == True

def test_fully_expanded_false():
    root = Node(None)
    node1 = Node(None, times_visited = 50)
    node2 = Node(None, times_visited = 0)
    node3 = Node(None, times_visited = 734)
    node4 = Node(None, times_visited = 42)
    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)
    assert fully_expanded(root) == False

def test_pick_unvisited():
    root = Node(None)
    node1 = Node(None, times_visited = 50)
    node2 = Node(None, times_visited = 0)
    node3 = Node(None, times_visited = 734)
    node4 = Node(None, times_visited = 0)
    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)
    assert pick_unvisited(root) in [node2,node4]

def test_traverse():
    root = Node(None,score = 30, times_visited = 2 )

    test_node = Node(None,score = 20, times_visited = 1)
    test_node.parent_node = root
    root.children.append(test_node)

    test_node_1 = Node(None, times_visited = 1)
    test_node_2 = Node(None, times_visited = 1)
    test_node_3 = Node(None, times_visited = 0)
    test_node_4 = Node(None, times_visited = 1)

    test_node.children.append(test_node_1)
    test_node.children.append(test_node_2)
    test_node.children.append(test_node_3)
    test_node.children.append(test_node_4)

    test_node_two = Node(None, score = 10, times_visited = 1)
    test_node_two.parent_node = root
    root.children.append(test_node_two)

    assert traverse(root) == test_node_3