def kruskal(IncidenceList):
    edges = generate_edge_list(IncidenceList)
    edges = sort_edges(edges)
    forest = UnionFind()
    forest.subsets = [0]*len(IncidenceList)
    forest.p = [0]*len(IncidenceList)
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
        self.p.append(-1)
        #self.p[vertice] = -len(self.subsets[vertice])

    def find_set(self, vertice):
        for tree in self.subsets:
            if vertice in tree:
                for other_vertice in tree:
                    if tree.index(other_vertice) < tree.index(vertice):
                        self.p[other_vertice] = "r"
        return "r"
        #return self.subsets[vertice]


    def get_root(self, subtree):
        pass

    def union(self, start,target):
        found_start_subtree, found_target_subtree = find_set(start), find_set(target)
        if found_start_subtree <= found_target_subtree:
            self.p(get_root(found_start_subtree)) = self.p(get_root(found_target_subtree))
            self.p(get_root(found_target_subtree)) = "size of combined tree"


#        store = self.subsets[start]
#        for vertice in range(len(self.subsets)):
#            if self.subsets[vertice] == store:
#                self.subsets[vertice] = self.subsets[target]
