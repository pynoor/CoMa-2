# TODO: define rotate_RL, rotate_LR, implement TikZ

import subprocess

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
        self.nodestyle = "circle, draw"
        self.edgestyle = "blue, very thick"
        self.root = None

    def __str__(self):

        commands = "blbal"

        BASIS = '\\documentclass[tikz]{{standalone}} \n\n\
        \\begin {{document}} \n\
         \\begin{{tikzpicture}}[every node/.style = {{{}}}, every edge/.style = {{draw, {}}}] \n\n\
          % Here go the sign commands. \n\
          {} \n\n\
         \\end{{tikzpicture}} \n\
        \\end{{document}}'

        BASIS.format(self.nodestyle, self.edgestyle, commands)

        return BASIS

    def getheight(self, node):

        if node == None:
            return -1
        else:
            return max(self.getheight(node.left), self.getheight(node.right)) + 1

    def repair_tree(self, node):
        if node.balance == -2 and node.left.balance in (0,-1):
            self.rotate_right(node)
            if node.left.balance == 0:
                node.balance = -1
                node.left.balance = 1
            else:
                node.balance = 0
                node.left.balance = 0
        elif node.balance == -2 and node.left.balance == 1:
            self.rotate_left_right(node)
            if node.left.right.balance == 0:
                node.balance = 0
                node.left.balance = 0
            elif node.left.right.balance == 1:
                node.balance = 0
                node.left.balance = -1
            elif node.left.right.balance == -1:
                node.balance = 1
                node.left.balance = 0
            node.left.right.balance = 0
        elif node.balance == 2 and node.right.balance in (0,1):
            self.rotate_left(node)
            if node.right.balance == 1:
                node.balance = 0
                node.right.balance = 0
            else:
                node.balance = 1
                node.right.balance = -1
        elif node.balance == 2 and node.right.balance == -1:
            self.rotate_right_left(node)
            if node.right.left.balance == 0:
                node.balance = 0
                node.right.balance = 0
            elif node.right.left.balance == 1:
                node.balance = -1
                node.left.balance = 0
            elif node.right.left.balance == -1:
                node.balance = 0
                node.left.balance = 1
            node.left.right.balance = 0

    def insert(self, key):
        # to do: implement insertion
        new_node = Node(key, None, None, None)
        y = None
        x = self.root
        while x != None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.p = y
        if y == None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        # traverse tree from new_node to T.root and repair
        node = new_node
        while self.root.key != node.key:
            if self.root.key < node.key:
                self.repair_tree(node)
                node = node.left
            else:
                self.repair_tree(node)
                node = node.right

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

    def rotate_left_right(self, node):
        self.rotate_left(node.left)
        self.rotate_right(node)

    def rotate_right_left(self, node):
        self.rotate_right(node.right)
        self.rotate_left(node)

    def visualize(self):
        #write str(self) in the avl.txt file
        subprocess.run(['touch', 'avl.txt'])
        with open('avl.txt', 'w') as file:
            file.write(str(self))

        #compile it by starting a pdflatex subprocess
        subprocess.run(['pdflatex avl.txt'])

        #show the produced pdf file in a viewer
        subprocess.run(['open avl.pdf'])



