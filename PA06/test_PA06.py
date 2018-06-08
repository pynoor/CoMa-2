import subprocess
from PA06 import SplayTree

def test_insert():
    # T = SplayTree(10, 10)
    process = subprocess.run(['python3 ~/Documents/GitHub/CoMa-2/PA06/PA06.py\nT = SplayTree(10,10)\nfor i in range(9, 4, -1):\n\    T.insert(i,i)'], stdout = subprocess.PIPE)
    result = process.stdout.read()
    # for i in range(9, 4, -1):
    #     T.insert(i, i)
    expected_result = 'Splay an Knoten: 9\n\
    2^Rotationen: 2\n\
    2^Potential vorher: 2\n\
    2^Potential nachher: 2\n\
    2^amortisierte Rotationen: 4/2\n\
    2^obere Schranke: 16/1\n\
    Splay an Knoten: 8\n\
    2^Rotationen: 2\n\
    2^Potential vorher: 3\n\
    2^Potential nachher: 6\n\
    2^amortisierte Rotationen: 12/3\n\
    2^obere Schranke: 54/1\n\
    Splay an Knoten: 7\n\
    2^Rotationen: 2\n\
    2^Potential vorher: 8\n\
    2^Potential nachher: 24\n\
    2^amortisierte Rotationen: 48/8\n\
    2^obere Schranke: 128/1\n\
    Splay an Knoten: 6\n\
    2^Rotationen: 2\n\
    2^Potential vorher: 30\n\
    2^Potential nachher: 120\n\
    2^amortisierte Rotationen: 240/30\n\
    2^obere Schranke: 250/1\n\
    Splay an Knoten: 5\n\
    2^Rotationen: 2\n\
    2^Potential vorher: 144\n\
    2^Potential nachher: 720\n\
    2^amortisierte Rotationen: 1440/144\n\
    2^obere Schranke: 432/1\n\ '
    assert result == expected_result


