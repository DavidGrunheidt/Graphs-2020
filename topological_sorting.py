from directed_graph import DirectedGraph
from strongly_connected_components import deepFirstSearchWithOrder

def topologialSort(graph: DirectedGraph) -> str:
    stack = list()
    visited = set()

    for vertex_id in graph.vertices:
        if vertex_id not in visited:
            deepFirstSearchWithInverseOrder(graph, vertex_id, stack, visited)

    stack_labels = list()
    for vertex_id in stack:
        stack_labels.append(graph.getVertexLabel(vertex_id))

    return ' -> '.join(stack_labels) + '\n'

def deepFirstSearchWithInverseOrder(graph: DirectedGraph, initial_vertex: str, stack: list, visited: set):
    visited.add(initial_vertex)

    for vertex_id in graph.getVertexNeighbors(initial_vertex):
        if vertex_id not in visited:
            deepFirstSearchWithInverseOrder(graph, vertex_id, stack, visited)

    stack.insert(0, initial_vertex)