def kruskal(IncidenceList):
    edges = generate_edge_list(IncidenceList)
    edges = sort_edges(edges)
    forest = UnionFind()
    p = forest.p
    vertex_count = len(IncidenceList)

    for vertex_id in range(vertex_count):
        forest.make_set()

    mintree = []
    for edge in edges:
        if vertex_count == 1:
            return mintree
        if forest.find_set(list(edge.incident)[0]) != forest.find_set(list(edge.incident)[1]):
            forest.union(list(edge.incident)[0], list(edge.incident)[1])
            p = forest.p
            mintree.append(edge)
            vertex_count -= 1
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


class UnionFind:

    def __init__(self):
        self.p = [] #list of root nodes

    def make_set(self):
        self.p.append(-1)

    def find_set(self, vertex):
        #can make this shorter
        vertex_id = vertex

        while self.p[vertex_id] >= 0:
            vertex_id = self.p[vertex_id]

        found_root = vertex_id

        vertex_id = vertex

        while vertex_id != found_root:
            #Pfadkompression
            store_value = self.p[vertex_id]
            self.p[vertex_id] = found_root
            vertex_id = store_value

        return found_root

    def union(self, start, target):

        found_start_set, found_target_set = self.find_set(start), self.find_set(target)

        if found_start_set == found_target_set:
            return

        if self.p[found_start_set] > self.p[found_target_set]:
            store_value = self.p[found_start_set]
            self.p[found_start_set] = found_target_set
            self.p[found_target_set] += store_value

        else:
            store_value = self.p[found_target_set]
            self.p[found_target_set] = found_start_set
            self.p[found_start_set] += store_value

