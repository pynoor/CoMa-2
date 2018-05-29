import PA04


def test_insert():
    #1)Construction
    tree = AVLTree(13)
    insert(17)
    insert(21)
    result = AVLTree.root.key
    expected_result = 17
    assert result == expected_result
