import json
from Vertex import Vertex
from Graph import Graph


def readin_data(filepath='courses.json'):
    """ A function that read in Json file """
    with open(filepath) as json_file:
        return json.load(json_file)


def jsonToGraph(filepath):
    """ takes a JSON file as input, and generates a graph """
    json_data = readin_data(filepath)
    for index, course in enumerate(json_data):  # Create all the vertices
        vertex = Vertex(index, course['name'])
        graph.add_vertex(vertex)

    for course in json_data:
        if len(course['prerequisites']) != 0:
            vertex = graph.find_vertex(course['name'])
            for prerequisite in course['prerequisites']:
                neighbor = graph.find_vertex(prerequisite)
                vertex.add_neighbor(neighbor)


graph = Graph()
jsonToGraph('courses.json')
result = graph.numPrereqs("FEW 2.3")
for course in result:
    print(course.data)
print(len(result)-1)
