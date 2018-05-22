def kruskal(IncidenceList):
    pass

def sort_edges(edges):
    output = sorted(edges, key = lambda x: x.w)
    return output

class Edge:

    __slots__ = ["incident", "w"]

    def __init__(self, start, target, weight):
        self.incident = {start, target}
        self.w = weight

