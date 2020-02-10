import pytest
from connect_four import Board
from monte_carlo import Node, ucb_scoring, traverse, best_move

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

#this function definitely needs to do something different than what i think it should do
def test_traverse():
    root = Node (None,score = 30, times_visited = 2 )
    test_node = Node(None,score = 20, times_visited = 1)
    test_node.parent_node = root
    test_node_two = Node(None, score = 10, times_visited = 1)
    test_node_two.parent_node = root
    root.children.append(test_node)
    root.children.append(test_node_two)
    assert traverse(root) == test_node

def test_best_move():
    root = Node(None)

    node1 = Node(None, times_visited = 50)
    node1.move_column = 0

    node2 = Node(None, times_visited = 100)
    node2.move_column = 1

    node3 = Node(None, times_visited = 734)
    node3.move_column = 2

    node4 = Node(None, times_visited = 42)
    node4.move_column = 3

    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)

    assert best_move(root) == 2