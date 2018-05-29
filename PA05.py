class Node:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.p = parent
        self.left = left
        self.right = right
        self.balance = 0

    def calculate_balance(self, Tree):
        left_child, right_child = self.left, self.right
        return Tree.getheight(right_child) - Tree.getheight(left_child)

    def is_balanced(self, Tree):
        if self.calculate_balance(Tree) in (1, -1, 0):
            return True
        else:
            return False

class AVLTree:
    def __init__(self, firstnodekey):
        self.insert(firstnodekey)
        self.root = firstnodekey
        self.nodestyle = "circle, draw"
        self.edgestyle = "blue, very thick"

    def __str__(self):
        pass

    def getheight(self, node):
        iterative_node = node
        height = 0
        while iterative_node != None and self.root != iterative_node.key:
            if self.root < iterative_node.key:
                iterative_node = iterative_node.left
            else:
                iterative_node = iterative_node.right
            height += 1
        return height


         # hereeeeee

    def balance_tree(self):
        pass

    def insert(self, key):
        new_node = Node(key, None, None, None)
        self.balance_tree()

    def tree_search(self, start_node, target_key):
        if start_node == None or target_key == start_node.key:
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

    def rotate_right(self, node):
        left_child = node.left
        if node.p == None:
            self.root = left_child
        elif node.p.left == node:
            node.p.left = left_child
        else:
            node.p.right = left_child
        left_child = node.p
        node.left = left_child.right
        if node.left != None:
            node.left.p = node
        left_child.right = node
        node.p = left_child

    def rotate_left(self, node):
        right_child = node.right
        if node.p == None:
            self.root = right_child
        elif node.p.left == node:
            node.p.left = right_child
        else:
            node.p.right = right_child
        right_child.p = node.p
        node.right = right_child.left
        if node.right != None:
            node.right.p = node
        right_child.left = node
        node.p = right_child





