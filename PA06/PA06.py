
class Node:
    def __init__(self, key, parent, left, right, data):
        self.key = key
        self.left = left
        self.right = right
        self.data = data
        self.p = parent

class SplayTree:
    def __init__(self, firstnodekey, firstnodedata):
        root = Node(firstnodekey, None, None, None, firstnodedata)
        self.firstnodekey = firstnodekey
        self.firstnodedata = firstnodedata
        self.root = root
        self.rotation_count = 0
        self.initial_potential = 0
        self.final_potential = 0
        self.amortised_rotations = 0
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

    def replace(self, node1, node2):
        if node1.p.left == node1:
            node1.p.left = node2
        else:
            node1.p.right = node2
        node2.p = node1.p

    def delete(self, key):
        node = self.search(key)

        #Case 1 : Node does not have children
        if node.left == None and node.right == None:
            if node.p.left == node:
                node.p.left = None
            else:
                node.p.right = None
            return

        #Case 2: Node has one child
        if node.left != None and node.right == None:
            self.replace(node, node.left)
            return

        elif node.left == None and node.right != None:
            self.replace(node, node.right)
            return

        #Case 3: Node has two children
        successor = self.tree_successor(node)
        if node.right == successor:
            self.replace(node, successor)
            return

        else:
            self.replace(successor, successor.right)
            self.replace(node, successor)



        # if node.left == None:
        #     self.transplant(node, node.right)
        # elif node.right == None:
        #     self.transplant(node, node.left)
        # else:
        #     min_right_subtree = self.tree_minimum(node.right)
        #     if min_right_subtree.p != node:
        #         self.transplant(min_right_subtree, min_right_subtree.right)
        #         min_right_subtree.right = node.right
        #         min_right_subtree.p = min_right_subtree
        #     self.transplant(node, min_right_subtree)
        #     min_right_subtree.left = node.left
        #     min_right_subtree.left.p = min_right_subtree

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
        iterative_node = node
        while node.left != None:
            iterative_node = node.left
        return iterative_node

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
