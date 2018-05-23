import PA04
from PA04 import kruskal
from PA04 import Edge
from PA04 import sort_edges
from PA04 import generate_edge_list
from PA04 import UnionFind


def test_kruskal_calculates_correct_edges():
    #1)Construction
    e1 = Edge(0,2,4)
    e2 = Edge(2,1,3)
    e3 = Edge(0,1,2)
    IncidenceList = [[e1, e3], [e2, e3], [e1, e2]]
    #2)Fantasize
    result = [e.incident for e in kruskal(IncidenceList)]
    #2)Verify
    expected_result = [{1,2}, {0,1}]
    assert result == expected_result

def test_sort_edges():
    #1) Concstruction
    e1 = Edge(0,2,4)
    e2 = Edge(2,1,3)
    e3 = Edge(0,1,2)
    edges = [e1, e2, e3]
    result = [x.w for x in sort_edges(edges)]
    expected_result = [2,3,4]
    assert result == expected_result

def test_generate_edge_list():
    e1 = Edge(0,2,4)
    e2 = Edge(2,1,3)
    e3 = Edge(0,1,2)
    IncidenceList = [[e1, e3], [e2, e3], [e1, e2]]
    result = set([edge.w for edge in generate_edge_list(IncidenceList)])
    expected_result = set([2, 3, 4])
    assert result == expected_result

def test_make_set():
    e1 = Edge(0,2,4)
    e2 = Edge(2,1,3)
    e3 = Edge(0,1,2)
    IncidenceList = [[e1, e3], [e2, e3], [e1, e2]]
    F = UnionFind()
    F.p = [0]*len(IncidenceList)
    for vertice in range(len(IncidenceList)):
        F.make_set(vertice)
    result = F.p
    expected_result = [0,1,2]
    assert result == expected_result