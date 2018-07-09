import pytest
from PA01 import Stack
from PA01 import Node
from PA01 import TopSort

def test_first_sample():
    n = Node()
    m = Node()
    n.name = "Quelle"
    m.name = "Senke"
    n.color = m.color = "white"
    n.successors = [m]
    m.successors = []
    G = [m, n]
    result = TopSort.topologische_sortierung(G)
    expected_result = ["Quelle", "Senke"]
    assert result == expected_result

def test_second_sample():
    n = Node()
    m = Node()
    n.name = "links"
    m.name = "rechts"
    n.color = m.color = "white"
    n.successors = [m]
    m.successors = [n]
    G = [m, n]
    result = TopSort.topologische_sortierung(G)
    expected_result = [-1]
    assert result == expected_result

def test_third_sample():
    a = Node()
    b = Node()
    c = Node()
    d = Node()
    e = Node()
    a.name = "eins"
    b.name = "zwei"
    c.name = "drei"
    d.name = "vier"
    e.name = "fünf"
    a.color = b.color = c.color = d.color = e.color = "white"
    a.successors = [b]
    b.successors = [c]
    c.successors = [d]
    d.successors = [e]
    e.successors = []
    G = [e,a,d,c,b]
    result = TopSort.topologische_sortierung(G)
    expected_result = ["eins","zwei","drei","vier","fünf"]
    assert result == expected_result