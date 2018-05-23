def kruskal(IncidenceList):
    edges = generate_edge_list(IncidenceList)
    edges = sort_edges(edges)
    F = UnionFind()
    F.p = [0]*len(IncidenceList)

    for vertice in range(len(IncidenceList)):
        F.make_set(vertice)
    B = []
    for edge in edges:
        if F.find_set(edge.incident[0]) != F.find_set(edge.incident[1]):
            F.union(edge.incident[0], edge.incident[1])
            B.append(edge)
    return B


def sort_edges(edges):
    output = sorted(edges, key = lambda x: x.w)
    return output

def generate_edge_list(IncidenceList):
    edges = []
    for incident_edge_list in IncidenceList:
        for edge in incident_edge_list:
            if edge not in edges:
                edges.append(edge)
    return edges

class Edge:

    __slots__ = ["incident", "w"]

    def __init__(self, start, target, weight):
        self.incident = [start, target]
        self.w = weight

class UnionFind:
    def __init__(self):
        self.p = [0]

    def make_set(self, vertice):
        self.p[vertice] = vertice

    def find_set(self, vertice):
        return self.p[vertice]

    def union(self, start,target):
        store = self.p[start]
        for vertice in range(1,len(self.p)):
            if self.p[vertice] == store:
                self.p[vertice] = self.p[target]
