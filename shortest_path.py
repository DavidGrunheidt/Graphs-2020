from graph import NotDirectedGraph

# Exercicio 4: Algoritmo de  Dijkstra
def dijkstra(graph: NotDirectedGraph, src_id: str) -> str:
    dists = dict()
    for vertex_id in graph.vertices:
        dists[vertex_id] = {'min_distance': float("inf"), 'parent': '-1', 'in_queue': True}
    dists[src_id] = {'min_distance': 0.0, 'parent': src_id, 'in_queue': True}

    for loopid in graph.vertices:
        min_dist_vertex_id = minDistanceVertexId(graph, dists, loopid)

        dists[min_dist_vertex_id]['in_queue'] = False

        for vertex_id in graph.vertices:
            weight_aux = graph.weight(min_dist_vertex_id, vertex_id)

            actual_min_dist = dists[vertex_id]['min_distance']
            calculated_min_dist = dists[min_dist_vertex_id]['min_distance']

            possible_new_min_dist = calculated_min_dist + weight_aux

            if weight_aux > 0 and dists[vertex_id]['in_queue'] and possible_new_min_dist < actual_min_dist:
                dists[vertex_id]['min_distance'] = possible_new_min_dist
                dists[vertex_id]['parent'] = min_dist_vertex_id

    return calculatedOutput(src_id, dists)

def minDistanceVertexId(graph: NotDirectedGraph, dists: dict, vid: str) -> str:
    min_vertex_id = vid
    min_dist = float('inf')

    for vertex_id in graph.vertices:
        if dists[vertex_id]['min_distance'] < min_dist and dists[vertex_id]['in_queue']:
            min_dist = dists[vertex_id]['min_distance']
            min_vertex_id = vertex_id

    return min_vertex_id

def calculatedOutput(src_id: str, dists: dict) -> str:
    output = ''

    for vertex_id in dists:
        output += vertex_id + ': '
        parent_vertex_id = dists[vertex_id]['parent']
        parent_lists = []
        if vertex_id == src_id:
            parent_lists += [vertex_id]
        else:
            parent_lists += [parent_vertex_id, vertex_id]
            while parent_vertex_id != src_id:
                parent_vertex_id = dists[parent_vertex_id]['parent']
                parent_lists.insert(0, parent_vertex_id)

        output += ','.join(parent_lists) + '; d = ' + str(dists[vertex_id]['min_distance']) + '\n'

    return output