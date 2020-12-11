class Graph:

    def __init__(self):
        """ Initialize a empty list to store vertices"""
        self.vertices = []

    def add_vertex(self, vertex):
        """ This method add a vertex into the list """
        self.vertices.append(vertex)

    def find_vertex(self, data):
        """ This method return the vertex 
        whose data value matches the data """
        for vertex in self.vertices:
            if vertex.data == data:
                return vertex

    def DFS(self, vertex, visited):
        """ This method recursively traverses down the vertices 
        and their neighbors"""
        visited.append(vertex)
        for id, neighbor_vertex in vertex.neighbors.items():
            if neighbor_vertex not in visited:  # Find nodes in neighbor list that hasn't been visited
                self.DFS(neighbor_vertex, visited)

    def numPrereqs(self, course_string):
        """ the method will return a path of the graph 
        with the starting point at the taken in course_string"""
        visited = []
        course_vertex = self.find_vertex(course_string)
        self.DFS(course_vertex, visited)

        return visited
