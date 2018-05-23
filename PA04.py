def kruskal(IncidenceList):
    edges = generate_edge_list(IncidenceList)
    edges = sort_edges(edges)
    forest = UnionFind()
    forest.subsets = [0]*len(IncidenceList)
    for vertice in range(len(IncidenceList)):
        forest.make_set(vertice)
    min_tree = []
    for edge in edges:
        if forest.find_set(list(edge.incident)[0]) != forest.find_set(list(edge.incident)[1]):
            forest.union(list(edge.incident)[0], list(edge.incident)[1])
            min_tree.append(edge)
    return min_tree


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

class UnionFind:
    def __init__(self):
        self.p = []
        self.subsets = []

    def make_set(self, vertice):
        self.subsets[vertice] = vertice

    def find_set(self, vertice):
        return self.subsets[vertice]

    def union(self, start,target):
        store = self.subsets[start]
        for vertice in range(len(self.subsets)):
            if self.subsets[vertice] == store:
                self.subsets[vertice] = self.subsets[target]
