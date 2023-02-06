import functools

class Node:

    def __init__(self, name):
        self._name = name
        self._edges = []

    def __add__(self, other_node):
        assert isinstance(other_node, Node), "Type not match"
        self._edges.append(other_node)

    def __sub__(self, other_node):
        assert isinstance(other_node, Node), "Type not match"
        self._edges.remove(other_node)
    def get_name(self):
        return self._name

class Graph:

    def __init__(self):
        self._nodes = []

    def __add__(self, other_node):
        assert isinstance(other_node, Node), "Type not match"
        self._nodes.append(other_node)

    def find(self, name):
        return [n for n in self._nodes if n.get_name == name].pop()

