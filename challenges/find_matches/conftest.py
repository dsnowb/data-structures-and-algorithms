from .k_tree import KTree, Node
import pytest


@pytest.fixture
def small_k_tree():
    tree = KTree(0)
    tree.root.children = [Node(i) for i in [11, 12, 11]]
    return tree


@pytest.fixture
def mid_k_tree():
    tree = KTree(0)
    tree.root.children = [Node(i) for i in [22, 12, 13]]
    tree.root.children[0].children = [Node(21), Node(22)]
    tree.root.children[1].children = [Node(23)]
    tree.root.children[2].children = [Node(i) for i in [22, 25, 26, 27]]
    tree.root.children[2].children[3].children = [Node(22), Node(32)]
    return tree
