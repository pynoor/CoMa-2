class Node:
    def __init__(self, key, leftchild, rightchild, data):
        self.key = key
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.data = data
class SplayTree:
    def __init__(self, firstnodekey, firstnodedata):
        firstnode = Node(firstnodekey, None, None, firstnodedata)
        self.insert(firstnode)
        self.firstnodekey = firstnodekey
        self.firstnodedata = firstnodedata
        self.root = firstnodekey

    def insert(self, node):
        pass
