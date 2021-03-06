import pytest
from board import Board
from monte_carlo import Node, ucb_scoring, traverse, best_move, best_ucb, fully_expanded, pick_unvisited, traverse, rollout_policy, rollout, is_root, monte_carlo_tree_search

board = Board()
board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '1', '?', '?', '?', '?', '?']]
board_move = 1
board.last_placed_row = 5
board.last_placed_column = 1
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
    #next line handled by get all children
    new_node.children = []
    new_child_node = Node(None)
    new_node.add_child(new_child_node)
    assert new_child_node in new_node.children  

def test_get_all_children():
    board_node.get_children_nodes()
    assert len(board_node.children) == 7

# Main Tree Search
def test_best_move():
    root = Node(None)
    root.children = []

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

# Traverse Tests
@pytest.mark.skip(reason="test uses 2 as c, currently using sqrt(2)")
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
    root.children = []
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
    root.children = []
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
    root.children = []
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
    root.children = []

    test_node = Node(None,score = 20, times_visited = 1)
    test_node.parent_node = root
    test_node.children = []
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

# Backpopogation tests
def test_is_root_true():
    root = Node(None)
    assert is_root(root) == True

def test_is_root_false():
    root = Node(None)
    node1 = Node(None, parent_node=root)
    assert is_root(node1) == False

# Error debugging
@pytest.mark.skip(reason="long runtime use as needed")
def test_bad_play():
    test_board = Board()
    test_board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '1', '?', '?', '?', '?'],
        ['2', '?', '2', '1', '?', '?', '?'],
        ['1', '?', '2', '2', '2', '?', '?'],
        ['1', '?', '1', '2', '2', '?', '?'],
        ['1', '2', '1', '1', '2', '1', '?']]
    assert  monte_carlo_tree_search(test_board,"1") == 4

@pytest.mark.skip(reason="long runtime use as needed")
def test_bad_play_winning_move():
    test_board = Board()
    test_board.board = [
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '2', '?', '?', '?'],
        ['?', '2', '1', '1', '?', '?', '?']]
    assert  monte_carlo_tree_search(test_board,"5") == 4

