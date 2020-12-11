
class Vertex:
    """ A node class for graph class to store data and its neighbors"""

    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data
        self.neighbors = {}  # A dict that stores all the connected vertices

    def add_neighbor(self, vertex):
        self.neighbors[vertex.id] = vertex
