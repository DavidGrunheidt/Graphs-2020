from graph import NotDirectedGraph
import sys

# Exercicio 4: Algoritmo de  Dijkstra
def dijkstra(graph: NotDirectedGraph, src_id: str) -> str:
    dists = dict()
    for vertex_id in graph.vertices:
        dists[vertex_id] = {'min_distance': float(sys.maxsize), 'path': [], 'calculated': False}
    dists[src_id] = {'min_distance': 0.0, 'path': [], 'calculated': False}

    for loop in graph.vertices:
        min_dist_vertex_id = minDistanceVertexId(graph, dists)

        dists[min_dist_vertex_id]['calculated'] = True

        for vertex_id in graph.vertices:
            weight_aux = graph.weight(min_dist_vertex_id, vertex_id)

            actual_min_dist = dists[vertex_id]['min_distance']
            calculated_min_dist = dists[min_dist_vertex_id]['min_distance']

            possible_new_min_dist = calculated_min_dist + weight_aux

            if weight_aux > 0 and not dists[vertex_id]['calculated'] and actual_min_dist > possible_new_min_dist:
                dists[vertex_id]['min_distance'] = possible_new_min_dist
                dists[vertex_id]['path'] += min_dist_vertex_id

    output = ''
    for vertex_id in dists:
        output += vertex_id + ': ' + ','.join(dists[vertex_id]['path']) + '; d = ' + str(dists[vertex_id]['min_distance']) + '\n'

    return output

def minDistanceVertexId(graph: NotDirectedGraph, dists: dict) -> str:
    min_vertex_id = 0
    min_dist = sys.maxsize

    for vertex_id in graph.vertices:
        if dists[vertex_id]['min_distance'] < min_dist and not dists[vertex_id]['calculated']:
            min_dist = dists[vertex_id]['min_distance']
            min_vertex_id = vertex_id

    return min_vertex_id