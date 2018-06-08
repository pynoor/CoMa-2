class Node:
    def __init__(self, key, left, right, data):
        self.key = key
        self.left = left
        self.right = right
        self.data = data
        self.p = None

class SplayTree:
    def __init__(self, firstnodekey, firstnodedata):
        self.insert(firstnodekey, firstnodedata)
        self.firstnodekey = firstnodekey
        self.firstnodedata = firstnodedata
        self.root = firstnodekey

    def insert(self, key, data):
        #this is just a placeholder to have an argument for self.splay
        new_node = Node(0, None, None, "foo")
        self.splay(new_node)
        pass

    def splaying_step(self, node):
        if node.p == None:
            return
        elif node.p.p == None and node == node.p.left:
            self.rotate_right(node.p)
        elif node.p.p == None and node == node.p.right:
            self.rotate_left(node.p)
        elif node == node.p.left and node.p == node.p.pleft:
            self.rotate_right(node.p.p)
            self.rotate_right(node.p)
        elif node == node.p.right and node.p == node.p.p.right:
            self.rotate_left(node.p.p)
            self.rotate_left(node.p)
        elif node == node.p.left and node.p == node.p.p.right:
            self.rotate_right_left(node.p.p)
        else:
            self.rotate_left_right(node.p.o)

    def splay(self, node):
        while node.p != None:
            self.splaying_step(node)

    def rotate_left(self, node):
        right = node.right
        if node.p == None:
            self.root = right
        elif node.p.left == node:
            node.p.left = right
        else:
            node.p.right = right
        right.p = node.p
        node.right = right.left
        if node.right != None:
            node.right.p = node
        right.left = node
        node.p = right

    def rotate_right(self, node):
        left = node.left
        if node.p == None:
            self.root = left
        elif node.p.left == node:
            node.p.left = left
        else:
            node.p.right = left
        left = node.p
        node.left = left.right
        if node.left != None:
            node.left.p = node
        left.right = node
        node.p = left

    def tree_search(self, start_node, target_key):
        if start_node == None or target_key == start_node.key:
            self.splay(start_node)
            return start_node
        if target_key < start_node.key:
            return self.tree_search(start_node.left, target_key)
        else:
            return self.tree_search(start_node.right, target_key)

    def transplant(self, node_1, node_2):
        if node_1.p == None:
            self.root = node_2
        elif node_1 == node_1.p.left:
            node_1.p.left = node_2
        else:
            node_1.p.right = node_2
        if node_2 !=  None:
            node_2.p = node_1.p

    def tree_delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            min_right_subtree = self.tree_minimum(node.right)
            if min_right_subtree.p != node:
                self.transplant(min_right_subtree, min_right_subtree.right)
                min_right_subtree.right = node.right
                min_right_subtree.p = min_right_subtree
            self.transplant(node, min_right_subtree)
            min_right_subtree.left = node.left
            min_right_subtree.left.p = min_right_subtree

        #repair tree

        while self.root.key != node.key:
            if self.root.key < node.key:
                self.repair_tree(node)
                node = node.left
            else:
                self.repair_tree(node)
                node = node.right

        if self.tree_successor(node) != None:
            successor = self.tree_successor(node)
            while self.root.key != successor.key:
                if self.root.key < successor.key:
                    self.repair_tree(successor)
                    successor = successor.left
                else:
                    self.repair_tree(node)
                    successor = successor.right


    def tree_minimum(self, node):
        iterative_node = node
        while node.left != None:
            iterative_node = node.left
        return iterative_node

    def tree_maximum(self, node):
        iterative_node = node
        while node.right != None:
            iterative_node = node.right
        return iterative_node

    def tree_successor(self, node):
        store_node = node
        if node.right != None:
            self.tree_minimum(node.right)
        successor = node.p
        while successor != None and store_node == successor.right:
            store_node = successor
            successor = successor.p
        return successor

    def tree_predecessor(self, node):
        store_node = node
        if node.left != None:
            self.tree_maximum(node.left)
        successor = node.p
        while successor != None and store_node == successor.left:
            store_node = successor
            successor = successor.p
        return successor

    def rotate_left_right(self, node):
        self.rotate_left(node.left)
        self.rotate_right(node)

    def rotate_right_left(self, node):
        self.rotate_right(node.right)
        self.rotate_left(node)

