from graph import NotDirectedGraph
from dijkstra import dijkstra

# Exercicio 4: Algoritmo de  Dijkstra
def floydWarshall(graph: NotDirectedGraph) -> str:
    output = ''
    for vertex_id in graph.vertices:
        output += vertex_id + ': '
        dists_dict = dijkstra(graph, vertex_id, False)
        dists_aux = list()
        for key in dists_dict:
            dists_aux.append(str(dists_dict[key]['min_distance']))
        output += ', '.join(dists_aux) + '\n'

    return output