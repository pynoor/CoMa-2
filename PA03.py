
def ford(Graph, r):

    def initialiseGraph(Graph):
        for node in Graph.nodes:
            node.y = float("inf")
            node.p = None

    initialiseGraph(Graph)
    r.y = 0

    def edges_are_balanced(Graph, edge):
        if edge.target.y > edge.start.y + edge.c:
            return False
        else:
            return True

    def balance_edges(Graph, edge):
        if not edges_are_balanced(Graph, edge):
            edge.target.y = edge.start.y + edge.c
            edge.target.p = edge.start

    for i in range(1, len(Graph.nodes)):
        next_edge = Graph.next_edge()
        while next_edge != None:
            balance_edges(Graph, next_edge)
            next_edge = Graph.next_edge()


    for edge in Graph.edges:
        if edge.target.y > edge.start.y + edge.c:
            return "This graph has cylces"

class Node:

    def __init__(self):
        self.y = float("inf")
        self.p = None
        self.outgoing = []

class Edge:

    def __init__(self, start = 0, target = 0, c = 0):
        self.start = start
        self.target = target
        self.c = c
        start.outgoing.append(self)


class AbstractGraph:

    def __init__(self, nodes = [], edges = []):
        self.nodes = nodes
        self.edges = edges

    def next_edge(self):
        pass

class DirectedGraph(AbstractGraph):

    def __init__(self, nodes = [], edges = [], permutated_edges = [], current_edge_index = "nonexistent"):
        AbstractGraph.__init__(self, nodes, edges)
        self.permutated_edges = (len(nodes) - 1) * edges
        self.current_edge_index = current_edge_index
        Node.color = "white"

    def next_edge(self):
        if self.current_edge_index == "nonexistent":
            self.current_edge_index = 0
            return self.permutated_edges[0]
        if self.current_edge_index == (len(self.permutated_edges) - 1):
            return None
        next_edge_index = self.current_edge_index + 1
        self.current_edge_index += 1
        return self.permutated_edges[next_edge_index]


def topologische_sortierung(Graph):
    #there will be no cycles so I could eventually remove the check up
    global found_cycle
    found_cycle = False
    nodes_list = []
    for node in Graph:
        if node.color == "white":
            topologische_sortierung_zwei(Graph, node, nodes_list)
            if found_cycle == True:
                return [-1]
    nodes_list.reverse()
    return nodes_list


def topologische_sortierung_zwei(Graph, node, nodes_list):
    global found_cycle
    node.color = "grey"
    for edge in node.outgoing:
        if edge.target.color == "grey":
            found_cycle = True
            return
        if edge.target.color == "white":
            topologische_sortierung_zwei(Graph, edge.target, nodes_list)
        if edge.target.color == "black":
            continue
    node.color = "black"
    nodes_list.append(node)
    return


class DAG(AbstractGraph):

    def __init__(self, nodes = [], edges = [], permutated_edges = [], current_edge_index = "nonexistent"):
        AbstractGraph.__init__(self, nodes, edges)
        self.permutated_edges = permutated_edges
        topologische_sortierung(self.nodes)
        for node in self.nodes:
            for edge in self.edges:
                if edge.start == node:
                    self.permutated_edges.append(edge)
        self.current_edge_index = current_edge_index

    def next_edge(self):
        if self.current_edge_index == "nonexistent":
            self.current_edge_index = 0
            return self.permutated_edges[0]
        if self.current_edge_index == (len(self.edges) - 1):
            return None
        next_edge_index = self.current_edge_index + 1
        self.current_edge_index += 1
        return self.permutated_edges[next_edge_index]
