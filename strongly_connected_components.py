from directed_graph import DirectedGraph

# Exercicio 1: Componentes fortemente conexas
def stronglyConnectedComponentes(graph: DirectedGraph) -> str:
    stack = list()
    visited = set()

    for vertex_id in graph.vertices:
        if vertex_id not in visited:
            deepFirstSearchWithOrder(graph, vertex_id, visited, stack)

    graph_reverse = transposeGraph(graph)
    visited = set()

    result_search = []

    while len(stack) > 0:
        vertex_id = stack.pop()
        if vertex_id not in visited:
            result_search.append(deepFirstSearch(graph_reverse, vertex_id, visited))

    return prettyPrintOutput(result_search)

def prettyPrintOutput(result_search: list) -> str:
    output = ''
    for line in result_search:
        output += ', '.join(line) + '\n'
    return output

def transposeGraph(graph: DirectedGraph) -> DirectedGraph:
    new_graph = DirectedGraph()

    for vertex_id in graph.vertices:
        new_graph.addVertex(vertex_id, graph.getVertexLabel(vertex_id))

    for vertex_id in graph.vertices:
        for vertex_neighbor_id in graph.getVertexNeighbors(vertex_id):
            new_graph.addEdge(vertex_neighbor_id, vertex_id, graph.weight(vertex_id, vertex_neighbor_id))

    return new_graph

def deepFirstSearchWithOrder(graph: DirectedGraph, init_vertex_id: str, visited: set, stack: list):
    visited.add(init_vertex_id)
    for vertex_id in graph.getVertexNeighbors(init_vertex_id):
        if vertex_id not in visited:
            deepFirstSearchWithOrder(graph, vertex_id, visited, stack)
    stack.append(init_vertex_id)

def deepFirstSearch(graph: DirectedGraph, init_vertex_id: str, visited: set) -> list:
    result_search = [init_vertex_id]
    visited.add(init_vertex_id)
    for vertex_id in graph.getVertexNeighbors(init_vertex_id):
        if vertex_id not in visited:
            result_search += deepFirstSearch(graph, vertex_id, visited)
    return result_search
