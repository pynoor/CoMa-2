#ERROR in visualize()

import subprocess

class Node:
    def __init__(self, key, parent, left, right):
        #initiates a new node with following attributes
        self.key = key
        self.p = parent
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self, firstnodekey):
        root = Node(firstnodekey, None, None, None)
        self.nodestyle = 'circle, draw'
        self.edgestyle = 'blue, very thick'
        self.root = root
        self.commands = ''

    def __str__(self):
        # returns a string representation of a tikz visualization of the tree in latex code
        self.command_builder(self.root, 0, 0, 2**self.getheight(self.root))
        # TODO: find a way to indent commands
        BASIS = \
        '\\documentclass[tikz]{{standalone}} \n\n\
        \\begin {{document}} \n\
         \\begin{{tikzpicture}}[every node/.style = {{{}}}, every edge/.style = {{draw, {}}}] \n\n\
            % Here go the sign commands. \n\
        {} \n\n\
          \\end{{tikzpicture}} \n\
        \\end{{document}}'

        return BASIS.format(self.nodestyle, self.edgestyle, self.commands)

    def node_command(self, node, x, y):
        return '\n\\coordinate(x{}) at ({},{}); \n\\node (n{}) at (x{}) {};'.format(node.key, x, y, node.key, node.key,'{$'+str(node.key)+'$}')

    def command_builder(self, node, x, y, height):
        # builds the tikz picture of the tree
        if node != None:
            self.commands += self.node_command(node, x, y)
            if node != self.root:
                self.commands += '\n\\draw (n{}) edge (n{}); \n'.format(node.p.key, node.key)
            self.command_builder(node.left, x - height, y - 2, height//2)
            self.command_builder(node.right, x + height, y - 2, height//2)

    def getbalance(self, node):
        if node == None:
            return 0
        else:
            return self.getheight(node.right) - self.getheight(node.left)

    def getheight(self, node):
        if node == None:
            return -1
        else:
            return max(self.getheight(node.left), self.getheight(node.right)) + 1

    def repair_tree(self, node):
        #repairs the balances of the tree by performing rotations
        while abs(self.getbalance(node)) > 1:
            if self.getbalance(node) < -1 and node.left != None:
                if self.getbalance(node.left) <= 0:
                    self.rotate_right(node)
                else:
                    self.rotate_left_right(node)
            elif self.getbalance(node) > 1 and node.right != None:
                if self.getbalance(node.right) >= 0:
                    self.rotate_left(node)
                else:
                    self.rotate_right_left(node)

    def insert(self, key):
        #inserts a new node in the tree in a way that the tree remains
        #an avl tree and repairs the balances
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
        while node != self.root:
            self.repair_tree(node)
            node = node.p
        self.repair_tree(self.root)

    def rotate_right(self, node):
        left_child = node.left
        if node.p == None:
            self.root = left_child
        elif node.p.left == node:
            node.p.left = left_child
        else:
            node.p.right = left_child
        left_child.p = node.p
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
        #subprocess.run(['touch', 'avl.txt'])
        with open('avl.tex', 'w') as file:
            file.write(str(self))
        #compile it by starting a pdflatex subprocess
        subprocess.call(['pdflatex', 'avl.tex'], stdout=subprocess.DEVNULL)
        #show the produced pdf file in a viewer
        subprocess.call(['open', 'avl.pdf'])



