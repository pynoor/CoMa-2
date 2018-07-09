import PA03
import pytest
from PA03 import Node
from PA03 import Edge
from PA03 import AbstractGraph
from PA03 import DirectedGraph
from PA03 import ford
from PA03 import DAG


def test_node_attribute_y_returns_shortest_path_length_1():
    #1) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    Graph = DirectedGraph(nodes, [e1, e2, e3, e4])
    ford(Graph, nodes[0])
    #2) Execution
    result = [node.y for node in nodes]
    #3) Assertion
    expected_result = [0, 1, 1, 2]
    assert result == expected_result

def test_node_attribute_y_returns_shortest_path_length_2():
    #1) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    Graph = DirectedGraph(nodes, [e1, e2, e3, e4])
    ford(Graph, nodes[1])
    #2) Execution
    result = [node.y for node in nodes]
    #3) Assertion
    expected_result = [float("inf"), 0, float("inf"), 3]
    assert result == expected_result


def test_node_attribute_p_returns_parent_in_shortest_path_1():
    #1) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    Graph = DirectedGraph(nodes, [e1, e2, e3, e4])
    ford(Graph, nodes[0])
    #2) Execution
    # result = [node.p for node in nodes]
    result = [node.p for node in nodes[:-3]]
    #3) Assertion
    #expected_result = [None , '<PA03.Node object at 0x10e25d8d0>', '<PA03.Node object at 0x10e25d8d0>', '<PA03.Node object at 0x10e25d668>']
    expected_result = [None]
    assert result == expected_result

def test_node_attribute_p_returns_parent_in_shortest_path_2():
    #1) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    Graph = DirectedGraph(nodes, [e1, e2, e3, e4])
    ford(Graph, nodes[1])
    #2) Execution
    # result = [node.p for node in nodes]
    result = [node.p for node in nodes[:-1]]
    #3) Assertion
    # expected_result = [None , None, None, '<PA03.Node object at 0x10233d3c8>']
    expected_result = [None, None, None]
    assert result == expected_result

def test_next_edge_for_directed_graph():
    #!) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    e1.name = 1
    e2.name = 2
    e3.name = 3
    e4.name = 4
    Graph = DirectedGraph(nodes, [e4, e3, e2, e1])
    a = Graph.next_edge().name
    b = Graph.next_edge().name
    c = Graph.next_edge().name
    d = Graph.next_edge().name
    e = Graph.next_edge().name
    f = Graph.next_edge().name
    g = Graph.next_edge().name
    h = Graph.next_edge().name
    i = Graph.next_edge().name
    j = Graph.next_edge().name
    k = Graph.next_edge().name
    l = Graph.next_edge().name

    #2) Fantasizing
    result = [a, b, c, d, e, f, g, h, i, j, k, l]
    #3) Asserting
    expected_result = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]
    assert result == expected_result

def test_next_edge_for_directed_graphs_raises_attribute_error_at_end_of_sequence():
    with pytest.raises(AttributeError):
        #!) Construction
        nodes = [Node() for number in range(4)]
        e1 = Edge(nodes[0], nodes[1], 1)
        e2 = Edge(nodes[0], nodes[2], 1)
        e3 = Edge(nodes[1], nodes[3], 3)
        e4 = Edge(nodes[2], nodes[3], 1)
        e1.name = 1
        e2.name = 2
        e3.name = 3
        e4.name = 4
        Graph = DirectedGraph(nodes, [e4, e3, e2, e1])
        Graph.next_edge()
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        #2) Fantasizing
        result = Graph.next_edge().name
        #3) Asserting
        expected_result = "foo"
        assert result == expected_result

def test_next_edge_for_acyclic_directed_graph():
    #!) Construction
    nodes = [Node() for number in range(4)]
    e1 = Edge(nodes[0], nodes[1], 1)
    e2 = Edge(nodes[0], nodes[2], 1)
    e3 = Edge(nodes[1], nodes[3], 3)
    e4 = Edge(nodes[2], nodes[3], 1)
    e1.name = 1
    e2.name = 2
    e3.name = 3
    e4.name = 4
    Graph = DAG(nodes, [e4, e3, e2, e1])
    a = Graph.next_edge().name
    b = Graph.next_edge().name
    c = Graph.next_edge().name
    d = Graph.next_edge().name
    #2) Fantasizing
    result = [a, b, c, d]
    #3) Asserting
    expected_result = [2, 1, 3, 4]
    assert result == expected_result

def test_next_edge_for_acyclic_directed_graph_raises_attribute_at_end_of_sequence():
    with pytest.raises(AttributeError):
    #!) Construction
        nodes = [Node() for number in range(4)]
        e1 = Edge(nodes[0], nodes[1], 1)
        e2 = Edge(nodes[0], nodes[2], 1)
        e3 = Edge(nodes[1], nodes[3], 3)
        e4 = Edge(nodes[2], nodes[3], 1)
        e1.name = 1
        e2.name = 2
        e3.name = 3
        e4.name = 4
        Graph = DAG(nodes, [e4, e3, e2, e1])
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        Graph.next_edge().name
        #2) Fantasizing
        result = Graph.next_edge().name
        #3) Asserting
        expected_result = "foo"
        assert result == expected_result