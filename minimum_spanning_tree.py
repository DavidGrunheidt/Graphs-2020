from not_directed_graph import NotDirectedGraph

#Prim's algorithm
def minimumSpanningTree(graph: NotDirectedGraph):
    min_spanning_tree = dict()

    first = True
    for vertex_id in graph.vertices:
        if first:
            first = False
            min_spanning_tree[vertex_id] = {'parent': None, 'weight': 0, 'visited': False}
        else:
            min_spanning_tree[vertex_id] = {'parent': None, 'weight': float('inf'), 'visited': False}

    for _ in graph.vertices:
        min_weight_vertex_id = getMinimumDistanceVertexId(graph, min_spanning_tree)
        min_spanning_tree[min_weight_vertex_id]['visited'] = True

        for vertex_id in graph.vertices:
            min_vertex = min_spanning_tree[vertex_id]

            actual_weight = 0
            has_edge = graph.hasEdge(min_weight_vertex_id, vertex_id)

            if has_edge:
                actual_weight = graph.weight(min_weight_vertex_id, vertex_id)

            if has_edge and actual_weight > 0 and not min_vertex['visited'] and min_vertex['weight'] > actual_weight:
                min_vertex['weight'] = actual_weight
                min_vertex['parent'] = min_weight_vertex_id

    return outputMinimumSpanningTree(graph, min_spanning_tree)


def getMinimumDistanceVertexId(graph: NotDirectedGraph, min_spanning_tree: dict) -> str:
    min_weight_vertex_id = ''
    min_weight = float('inf')

    for vertex_id in graph.vertices:
        vertex_weight = min_spanning_tree[vertex_id]['weight']
        vertex_visited = min_spanning_tree[vertex_id]['visited']
        if vertex_weight < min_weight and not vertex_visited:
            min_weight = vertex_weight
            min_weight_vertex_id = vertex_id

    return min_weight_vertex_id

def outputMinimumSpanningTree(graph: NotDirectedGraph, min_spanning_tree: dict) -> str:
    sum_weight = 0
    path_list = list()

    for vertex_id in graph.vertices:
        parent_vertex_id = min_spanning_tree[vertex_id]['parent']
        if parent_vertex_id is not None:
            path_list.append(str(parent_vertex_id) + '-' + str(vertex_id))
            sum_weight += min_spanning_tree[vertex_id]['weight']

    output = str(sum_weight) + '\n'
    output += ', '.join(path_list)
    return output