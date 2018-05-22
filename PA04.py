def kruskal(IncidenceList):
    pass

class Edge:
    def __init__(self, start, target, weight):
        self.incident = {start, target}
        self.w = weight
