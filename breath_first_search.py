from not_directed_graph import NotDirectedGraph

# Exercicio 2: Busca em largura
def breadthFirstSearch(graph: NotDirectedGraph, inital_vertex_id: str) -> (str, set):
    visited = set()
    queue = [inital_vertex_id]
    search = ''
    level = 0

    while len(queue) > 0:
        # nodeCount (queue size). Indicates number of nodes at current level.
        count = len(queue)

        search += str(level) + ': '

        # Dequeue all nodes of current level and enqueue all nodes of next level.
        while count > 0:
            neighbor_id = queue.pop(0)
            count -= 1
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                queue += [x for x in graph.getVertexNeighbors(neighbor_id) if x not in visited and x not in queue]
                search += neighbor_id + ' '
        search += '\n'
        level += 1

    return search, visited
