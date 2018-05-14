import PA02
from PA02 import DIN5007_1
from PA02 import DIN5007_2
from PA02 import Liste
from PA02 import heapsort
from PA02 import max_heapify
from PA02 import build_max_heap
import pytest

def cmp_din5007_1(str1 ,str2):
    a = str1.string.casefold().replace("ä", "a").replace("ö", "o").replace ("ü", "u")
    b = str2.string.casefold().replace("ä", "a").replace("ö", "o").replace ("ü", "u")
    return a <= b

def cmp_din5007_2 (str1, str2):
    a = str1.string.casefold().replace("ä", "ae").replace("ö", "oe").replace ("ü", "ue")
    b = str2.string.casefold().replace("ä", "ae").replace("ö", "oe").replace ("ü", "ue")
    return a <= b

def test_DIN5007_1_comparison():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    result = (str1 <= str2)
    expected_result = False
    assert result == expected_result

def test_DIN5007_2_comparison():
    str1 = DIN5007_2("Jäger")
    str2 = DIN5007_2("jagen")
    result = (str1 <= str2)
    expected_result = True
    assert result == expected_result

def test_length_of_list():
    str1 = DIN5007_1("one")
    str2 = DIN5007_1("two")
    str3 = DIN5007_1("three")
    L = Liste([str1, str2, str3])
    result = len(L)
    expected_result = 3
    assert result == expected_result

def test_Liste_index_returns_storage_location():
    str1 = DIN5007_1("one")
    str2 = DIN5007_1("two")
    str3 = DIN5007_1("three")
    L = Liste([str1, str2, str3])
    result = L[1]
    expected_result = L[1]
    assert result == expected_result

def test_list_gets_first_object():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    L = Liste([str1, str2])
    result = str(L[1])
    expected_result = "Jäger"
    assert result == expected_result

def test_list_gets_second_object():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    L = Liste([str1, str2])
    result = str(L[2])
    expected_result = "jagen"
    assert result == expected_result

def test_list_returns_error_trying_to_get_zeroth_object():
    with pytest.raises(IndexError):
        str1 = DIN5007_1("Jäger")
        str2 = DIN5007_1("jagen")
        L = Liste([str1, str2])
        result = str(L[0])
        expected_result = IndexError
        assert result == expected_result

def test_list_swp():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    L = Liste([str1, str2])
    L.swp(1, 2)
    result = str(L)
    expected_result = "['jagen', 'Jäger']"
    assert result == expected_result

def test_max_heapify():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    L = Liste([str1, str2])
    max_heapify(L, 2, count = 1)
    result = L.l
    expected_result = [str1, str2]
    assert result == expected_result

def test_heapify():
    str1 = DIN5007_1("Jäger")
    str2 = DIN5007_1("jagen")
    L = Liste([str1, str2])
    heapsort(L)
    result = str(L)
    expected_result = "['jagen', 'Jäger']"
    assert result == expected_result

