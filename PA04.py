def kruskal(IncidenceList):
    edges = generate_edge_list(IncidenceList)
    edges = sort_edges(edges)
    forest = UnionFind()

    for vertex_id in range(len(IncidenceList)):
        forest.make_set()

    mintree = []
    for edge in edges:
        if forest.find_set(list(edge.incident)[0]) != forest.find_set(list(edge.incident)[1]):
            forest.union(list(edge.incident)[0], list(edge.incident)[1])
            mintree.append(edge)
    return mintree


def sort_edges(edges):
    return sorted(edges, key = lambda x: x.w)

def generate_edge_list(IncidenceList):
    edges = set()
    for incident_edge_list in IncidenceList:
        for edge in incident_edge_list:
            if edge not in edges:
                edges.add(edge)
    return list(edges)

class Edge:
    __slots__ = ["incident", "w"]
    def __init__(self, start, target, weight):
        self.incident = {start, target}
        self.w = weight

class Node:
    def __init__(self, id, height_in_tree, parent):
        self.height_in_tree = height_in_tree
        self.id = id
        self.parent = parent

class UnionFind:

    def __init__(self):
        self.node_list = [] #list of vertices
        self.p = [] #list of root nodes
        self.subtrees = []

    def make_set(self):
        self.p.append(-1)
        new_node_id = len(self.p) - 1
        new_node = Node(new_node_id, self.p[new_node_id], None)
        self.node_list.append(new_node)
        self.subtrees.append(new_node)

    def find_set(self, node_id):
        #can make this shorter
        iteration_node = self.node_list[node_id]

        while iteration_node.parent != None:
            iteration_node = iteration_node.parent

        found_root = iteration_node

        iteration_node = self.node_list[node_id]

        while iteration_node != found_root:
            #Pfadkompression
            store_iteration_node_parent = iteration_node.parent
            iteration_node.parent = found_root
            iteration_node = store_iteration_node_parent

            #hier
            print(iteration_node.id)
            print(self.p)
            self.p[iteration_node.id] = found_root.id

        return found_root.id

    def union(self, start, target):
        found_start_set, found_target_set = self.find_set(start), self.find_set(target)
        if found_start_set < found_target_set:
            self.node_list[found_start_set].parent = self.node_list[found_target_set]
            store_value = self.p[found_start_set]
            self.p[found_start_set] = self.p[found_target_set]
            self.p[found_target_set] += store_value
            self.subtrees.remove(self.subtrees[found_start_set])
        else:
            self.node_list[found_target_set].parent = self.node_list[found_start_set]
            self.subtrees.remove(self.subtrees[found_target_set])
            if found_start_set == found_target_set:
                self.p[found_start_set] += self.p[found_target_set] + 1
