import tkinter
from tkinter import *

class Node:
    def __init__(self, key, parent, left, right, data):
        self.key = key
        self.left = left
        self.right = right
        self.data = data
        self.p = parent

class SplayTree:
    def __init__(self, firstnodekey, firstnodedata):
        self.root = Node(firstnodekey, None, None, None, firstnodedata)
        self.rotation_count = 0
        self.upper_boundary = ''

    def traverse(self, node):
        tree = []
        def inorder_tree_walk(node):
            if node != None:
                inorder_tree_walk(node.left)
                tree.append(node)
                inorder_tree_walk(node.right)
        inorder_tree_walk(node)
        return tree

    def search(self, key):
        start = self.root
        store_start = start
        while start != None and key != start.key:
            store_start = start
            if key < start.key:
                start = start.left
            else:
                start = start.right

        if start == None:
            self.Splay(store_start)
            return start
        else:
            self.Splay(start)
            return start

        def search_help(start, target):
            if start == None or key == start.key:
                return start
            if key < start.key:
                return search_help(start.left, key)
            else:
                return search_help(start.right, key)
        found_node = search_help(self.root, key)
        if found_node != None:
            self.Splay(found_node)
        return found_node

    def insert(self, key, data):
        #inserts a new node into the splay tree
        new_node = Node(key, None, None, None, data)
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
        self.Splay(new_node)

    def splaying_step(self, node):
        rotation_count = 0
        if node.p == None:
            return
        elif node.p.p == None and node == node.p.left:
            self.rotate_right(node.p)
            rotation_count += 1
        elif node.p.p == None and node == node.p.right:
            self.rotate_left(node.p)
            rotation_count += 1
        elif node == node.p.left and node.p == node.p.p.left:
            self.rotate_right(node.p.p)
            self.rotate_right(node.p)
            rotation_count += 2
        elif node == node.p.right and node.p == node.p.p.right:
            self.rotate_left(node.p.p)
            self.rotate_left(node.p)
            rotation_count += 2
        elif node == node.p.left and node.p == node.p.p.right:
            self.rotate_right(node.p)
            self.rotate_left(node.p)
            rotation_count += 2
        else:
            self.rotate_left(node.p)
            self.rotate_right(node.p)
            rotation_count += 2
        return rotation_count


    def calculate_potential(self):
        product = 1
        for node in self.traverse(self.root):
            product *= len(self.traverse(node))
        return product

    def Splay(self, node):
        store_initial_potential = self.calculate_potential()
        store_nodes_initial_subtree_count = len(self.traverse(node))
        self.rotation_count = 0
        self.upper_boundary = ''
        while node.p != None:
            self.rotation_count += self.splaying_step(node)
        store_final_potential = self.calculate_potential()
        self.upper_boundary = str(2*(len(self.traverse(self.root)))**3)+ '/'+ str((store_nodes_initial_subtree_count)**3)
        print('Splay an Knoten: '+str(node.key))
        print('2^Rotationen: '+str(2**self.rotation_count))
        print('2^Potential vorher: '+str(store_initial_potential))
        print('2^Potential nachher: '+str(store_final_potential))
        print('2^amortisierte Rotationen: ' +str((2**self.rotation_count)*store_final_potential)+'/'+str(store_initial_potential))
        print('2^obere Schranke: ' + self.upper_boundary)
        self.rotation_count = 0
        self.upper_boundary = ''

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
        left.p = node.p
        node.left = left.right
        if node.left != None:
            node.left.p = node
        left.right = node
        node.p = left

    def transplant(self, node_1, node_2):
        if node_1.p == None:
            self.root = node_2
        elif node_1 == node_1.p.left:
            node_1.p.left = node_2
        else:
            node_1.p.right = node_2
        if node_2 != None:
            node_2.p = node_1.p


    def delete(self, key):
        if self.root.left == None and self.root.right == None:
            return
        node = self.search(key)
        if node != None:
            if node.left == None:
                self.transplant(node, node.right)
            elif node.right == None:
                self.transplant(node, node.left)
            else:
                y = self.tree_minimum(node.right)
                if y.p != node:
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.p = y
                self.transplant(node, y)
                y.left = node.left
                y.left.p = y
        else:
            return

    def tree_successor(self, node):
        store_node = node
        if node.right != None:
            self.tree_minimum(node.right)
        successor = node.p
        while successor != None and store_node == successor.right:
            store_node = successor
            successor = successor.p
        return successor

    def tree_minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def tree_maximum(self, node):
        iterative_node = node
        while node.right != None:
            iterative_node = node.right
        return iterative_node

    def rotate_left_right(self, node):
        self.rotate_left(node.left)
        self.rotate_right(node)

    def rotate_right_left(self, node):
        self.rotate_right(node.right)
        self.rotate_left(node)

    def getheight(self, node):
        if node == None:
            return -1
        else:
            return max(self.getheight(node.left), self.getheight(node.right)) + 1

    def draw(self, canvas):

        self.canvas = canvas

        self.canvas_height = canvas.winfo_reqheight()
        self.canvas_width = canvas.winfo_reqwidth()

        half_rect_width = 30
        half_rect_height = 15

        width_position = self.canvas_width//2
        height_position = 20

        def recursive_drawer(node, width_position, height_position):
            canvas.create_rectangle(width_position - half_rect_width, height_position + half_rect_height, width_position + half_rect_width, height_position - half_rect_height, fill = 'grey')
            canvas.create_text(width_position, height_position, text = str(node.key))
            if node.left != None:
                print('is left neighbour')
                initial_width_position = width_position
                initial_height_position = height_position
                width_position -= 35
                height_position += 35
                canvas.create_line(initial_width_position + half_rect_width, initial_height_position + half_rect_height, width_position + half_rect_width, height_position - half_rect_height)
                recursive_drawer(node.left, width_position, height_position)
            if node.right != None:
                initial_width_position = width_position
                initial_height_position = height_position
                width_position += 35
                height_position += 35
                canvas.create_line(initial_width_position + half_rect_width, initial_height_position + half_rect_height, width_position + half_rect_width, height_position - half_rect_height)
                recursive_drawer(node.right, width_position, height_position)

        recursive_drawer(self.root, width_position, height_position)



class TreeVisualizer:
    def __init__(self, root):
        self.root = root

        self.root.title('Welcome')

        #create main frames
        self.entry_frame = Frame(self.root)
        self.button_frame = Frame(self.root)
        self.canvas_frame = Frame(self.root)

        #layout main frames
        self.entry_frame.grid(row = 0)
        self.button_frame.grid(row = 1)
        self.canvas_frame.grid(row = 2)


        #create entry fields for key and data
        key_label = Label(self.entry_frame, text = 'Enter key')
        data_label = Label(self.entry_frame, text = 'Enter data')
        self.key_entry = Entry(self.entry_frame)
        self.data_entry = Entry(self.entry_frame)


        #layout entry fields in entry frame
        key_label.grid(row = 0, column = 0)
        data_label.grid(row = 0, column = 1)
        self.key_entry.grid(row = 1, column = 0)
        self.data_entry.grid(row = 1, column = 1)

        #create construct button
        self.construct_button = Button(self.button_frame, text = 'construct', fg = 'blue',
        command = lambda:self.construct(int(self.key_entry.get()), self.data_entry.get()))

        self.construct_button.grid(row = 0, column = 1)

    def construct(self, key, data):

        #create Class variable that points to the tree in question
        self.Tree = SplayTree(key, data)

        #destroy 'construct' button
        self.construct_button.destroy()

        #create canvas object
        self.canvas = Canvas(self.canvas_frame, width = 1000, height = 1000)
        self.canvas.grid(row = 0)

        #draw tree using SplayTree method 'draw', passing the previously
        #created canvas object as argument
        self.Tree.draw(self.canvas)

        #create insert button
        self.insert_button = Button(self.button_frame, text = 'insert', fg = 'blue',
        command = lambda:self.insert(int(self.key_entry.get()), self.data_entry.get()))
        self.insert_button.grid(row = 0, column = 0)

        #create search button
        self.search_button = Button(self.button_frame, text = 'search', fg = 'blue',
        command = lambda:self.search(int(self.key_entry.get())))
        self.search_button.grid(row = 0, column = 1)

        #create delete button
        self.delete_button = Button(self.button_frame, text = 'delete', fg = 'blue',
        command = lambda:self.delete(int(self.key_entry.get())))
        self.delete_button.grid(row = 0, column = 2)

    def insert(self, key, data):

        #insert node using SplayTree method 'insert'
        self.Tree.insert(key, data)

        #destroy existing canvas
        self.canvas.destroy()

        #create new empty canvas
        self.canvas = Canvas(self.canvas_frame, width = 1000, height = 1000)
        self.canvas.grid(row = 0)

        #draw the new tree (resulting from the insertion) into the canvas
        #using SplayTree method 'draw'
        self.Tree.draw(self.canvas)


    def search(self, key):

        #search for node that has the required key using SplayTree
        #method 'search' and store result in variable 'result'
        result = self.Tree.search(key)

        #delete all nodes in canvas object
        self.canvas.delete('all')

        #draw new Tree resulting from search operation
        self.Tree.draw(self.canvas)

        #if the found node is 'None', return string 'None'
        if result == None:
            print('None')

        #else return the key and the data of the found node in the
        #following string
        else:
            print('Node with key: ' + str(result.key) + ' and data: ' + str(result.data))


    def delete(self, key):

        #delete node with argument key in the Tree using the SplayTree
        #method 'delete'
        self.Tree.delete(key)

        #destroy the existing canvas
        self.canvas.destroy()

        #create a new empty canvas
        self.canvas = Canvas(self.canvas_frame, width = 1000, height = 1000)
        self.canvas.grid(row = 0)

        #draw the new Tree (resulting from the deletion) into the canvas
        #using SplayTree method 'draw'
        self.Tree.draw(self.canvas)

