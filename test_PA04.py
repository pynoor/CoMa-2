import PA04

def kruskal_calculates_correct_edges():
    #1)Construction
    e1 = Edge(0,2,4)
    e2 = Edge(2,1,3)
    e3 = Edge(0,1,2)
    #2)Fantasize
    result = [e.incident for e in kruskal(I)]
    #2)Verify
    expected_result = [{1,2}, {0,1}]
    assert expected_result == result