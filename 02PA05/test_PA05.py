import PA05
from PA05 import Node
from PA05 import AVLTree


def test_insert():
    #1)Construction
    tree = AVLTree(13)
    tree.insert(17)
    tree.insert(21)
    result = tree.root
    expected_result = 17
    assert result == expected_result
