
class Stack:

     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Node:

    def __init__(self, successors = [], name = "" ,  color = "white"):
        self.successors = successors
        self.name = name
        self.color = color


class TopSort:

    @staticmethod
    def topologische_sortierung(G):
        global found_cycle
        found_cycle = False
        nodes_list = []
        for node in G:
            if node.color == "white":
                TopSort.topologische_sortierung_zwei(G, node, nodes_list)
                if found_cycle == True:
                    return [-1]

        nodes_list.reverse()
        return [s.name for s in nodes_list]

    @staticmethod
    def topologische_sortierung_zwei(G, node, nodes_list):
        global found_cycle
        node.color = "grey"
        for neighbour in node.successors:
            if neighbour.color == "grey":
                found_cycle = True
                return
            if neighbour.color == "white":
                TopSort.topologische_sortierung_zwei(G, neighbour, nodes_list)
            if neighbour.color == "black":
                continue

        node.color = "black"
        nodes_list.append(node)
        return



