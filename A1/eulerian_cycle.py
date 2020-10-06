import random

from graph import NotDirectedGraph
from breath_first_search import breadthFirstSearch

# Exercicio 3: Ciclo Euleriano
def getEulerianTour(graph: NotDirectedGraph) -> str:
    eulerian_type = getEulerianType(graph)
    output = str(int(eulerian_type != 0))

    if eulerian_type == 0:
        return output

    initial_vertex_id = find_initial_vertex_id(graph)

    graph_copy = graph.copy()

    output += '\n'
    output += ','.join(calculateEulerianTour(graph_copy, initial_vertex_id))

    return output

def isValidNextEdge(graph: NotDirectedGraph, vertex1_id: str, vertex2_id: str) -> bool:
    if len(graph.getVertexNeighbors(vertex1_id)) == 1:
        return True

    # Is v1 <-> v2 a bridge ? count1 > count2 , then yes.
    count1 = len(breadthFirstSearch(graph, vertex1_id)[1])
    graph.removeEdge(vertex1_id, vertex2_id)
    count2 = len(breadthFirstSearch(graph, vertex1_id)[1])

    # Put back this edge
    graph.addEdge(vertex1_id, vertex2_id, 0.0)

    return count1 == count2

def calculateEulerianTour(graph: NotDirectedGraph, vertex_id: str) -> list:
    neighbors = graph.getVertexNeighbors(vertex_id).copy()

    if graph.getNumberOfEdges() == 0:
        return [vertex_id]

    partial_tour = []
    for neighbor_id in neighbors:
        if graph.getNumberOfEdges() == 0:
            break
        elif isValidNextEdge(graph, vertex_id, neighbor_id):
            graph.removeEdge(vertex_id, neighbor_id)
            partial_tour += [vertex_id] + calculateEulerianTour(graph, neighbor_id)

    return partial_tour

def find_initial_vertex_id(graph: NotDirectedGraph) -> str:
    for vertex_id in graph.vertices:
        if graph.getVertexDegree(vertex_id) % 2 == 1:
            return vertex_id
    return random.choice(list(graph.vertices))

def isConnected(graph: NotDirectedGraph) -> bool:
    visited_vertices = breadthFirstSearch(graph, random.choice(list(graph.vertices)))[1]
    number_of_vertices = graph.getNumberOfVertices()

    return len(visited_vertices) == number_of_vertices

# 0 -> False; 1 -> Euler Path (Semi-Eulerian); 2 -> Euler Cycle (Eulerian)
def getEulerianType(graph: NotDirectedGraph) -> int:
    if not isConnected(graph):
        return 0

    odd = 0
    for vertex_id in graph.vertices:
        if graph.getVertexDegree(vertex_id) % 2 != 0:
            odd += 1
            if odd > 2:
                return 0

    if odd == 0:
        return 2
    else:
        return 1
