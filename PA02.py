
import math

def heapsort(L):
    count = len(L)
    build_max_heap(L, count)
    while count > 1:
        L.swp(1, count)
        count -= 1
        max_heapify(L, 1, count)

def max_heapify(L, parent, count):
    largest = 0
    left_child = 2 * parent
    right_child = 2 * parent + 1
    if left_child <= count and (not L[left_child] <= L[parent]):
        largest = left_child
    else:
        largest = parent
    if right_child <= count and (not L[right_child] <= L[largest]):
        largest = right_child
    if largest != parent:
        L.swp(parent, largest)
        max_heapify(L, largest, count)

def build_max_heap(L, count):
    for i in range(math.floor((len(L)/2)), 0, -1):
        max_heapify(L, i, count)

class Liste:
    def __init__(self, l):
        self.l = l

    def __getitem__(self, i):
        if i <= 0:
            raise IndexError
        return self.l[i-1]

    def __len__(self):
        return len(self.l)

    def __str__(self):
        #string repräsentation muss ein string sein ?
        return str([str(x) for x in self.l])

    def swp(self, i, j):
        self.l[i-1], self.l[j-1] = self.l[j-1], self.l[i-1]


class DIN5007_1:
    def __init__(self, s):
        self.s = s

    def __le__(self, f):
        # I think this is where the attribute error is coming from ...
        a = self.s.casefold().replace("ä", "a").replace("ö", "o").replace ("ü", "u")
        b = f.s.casefold().replace("ä", "a").replace("ö", "o").replace ("ü", "u")
        return a <= b

    def __str__(self):
        return str(self.s)



class DIN5007_2:
    def __init__(self, s):
        self.s = s

    def __le__(self, f):
        a = self.s.casefold().replace("ä", "ae").replace("ö", "oe").replace ("ü", "ue")
        b = f.s.casefold().replace("ä", "ae").replace("ö", "oe").replace ("ü", "ue")
        return a <= b

    def __str__(self):
        return str(self.s)


