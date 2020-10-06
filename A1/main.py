import os
import sys
import random

from graph import NotDirectedGraph
from graph_builder import buildGraphFromFile
from breath_first_search import breadthFirstSearch
from eulerian_cycle import getEulerianTour
from dijkstra import dijkstra
from floyd_warshall import floydWarshall


# on the first call to this function you must be SURE that "path" exists in the actual os.listdir()
def buildEachInstance(path: str) -> 'dict of Graphs':
	graphs = dict()

	# go into folder
	os.chdir(path)

	for item in os.listdir():
		if os.path.isdir(item):
			graphs.update(buildEachInstance(item))
		else: 
			graphs[item] = buildGraphFromFile(item)

	# return to the initial folder
	os.chdir("..")

	return graphs

# run all implemented algorithms on some graph
def test_graph(path: str, graph: NotDirectedGraph) -> None:
	print('\nTest Results for Graph in ' + path + ':\n')

	rand_vertex_id = random.choice(list(graph.vertices.keys()))
	rand_vertex_name = graph.getVertexLabel(rand_vertex_id)
	rand_vertex_neighbors = graph.getVertexNeighbors(rand_vertex_id)
	rand_vertex_rand_neighbor = random.choice(list(rand_vertex_neighbors))
	other_rand_vertex_id0 = random.choice(list(graph.vertices.keys()))
	other_rand_vertex_id1 = random.choice(list(graph.vertices.keys()))

	print('Number of vertices = ' + str(graph.getNumberOfVertices()))
	print('Number of edges = ' + str(graph.getNumberOfEdges()))
	print('Vertex ' + rand_vertex_id + ' degree = ' + str(graph.getVertexDegree(rand_vertex_id)))
	print('Vertex ' + rand_vertex_id + ' name = ' + rand_vertex_name)
	print('Vertex ' + rand_vertex_id + ' neighbors = ' + str(rand_vertex_neighbors))
	print('Vertex ' + rand_vertex_id + ' has edge with ' + rand_vertex_rand_neighbor + ' = ' + str(graph.hasEdge(rand_vertex_id, rand_vertex_rand_neighbor)))
	print('Vertex ' + rand_vertex_id + ' has edge with ' + other_rand_vertex_id0 + ' = ' + str(graph.hasEdge(rand_vertex_id, other_rand_vertex_id0)))
	print('Vertex ' + rand_vertex_id + ' has edge with ' + other_rand_vertex_id1 + ' = ' + str(graph.hasEdge(rand_vertex_id, other_rand_vertex_id1)))
	print('Edge ' + rand_vertex_id + ' <-> ' + rand_vertex_rand_neighbor + ' weight(s) = ' + str(graph.weight(rand_vertex_id, rand_vertex_rand_neighbor)))

def main():
	maybePath = sys.argv[len(sys.argv)-1]

	if maybePath == "testAll":
		graphs = buildEachInstance("instances")

		for graph in graphs:
			if len(graphs[graph].vertices) == 0:
				print("Graph in " + graph + ' has a problem')
				return

		print("Nothing wrong with the inputs.\n")
	else:
		# Exercicio 1:
		print('Exercicio 1 (Funções De Grafos):')
		graph_path = "./instances/caminho_minimo/fln_pequena.net"
		graph = buildGraphFromFile(graph_path)
		test_graph(graph_path, graph)

		# Exercicio 2:
		print('\nExercicio 2 (Busca em largura):\n')
		print(breadthFirstSearch(graph, '1')[0])

		# Exercicio 3:
		print('\nExercicio 3 (Ciclo Euleriano):\n')
		graph_path = "./instances/ciclo_euleriano/ContemCicloEuleriano.net"
		graph = buildGraphFromFile(graph_path)
		print(getEulerianTour(graph))

		# Exercicio 4:
		print('\nExercicio 4 (Dijkstra):\n')
		graph_path = "./instances/caminho_minimo/fln_pequena.net"
		graph = buildGraphFromFile(graph_path)
		print(dijkstra(graph, '1', True))

		# Exercicio 5:
		print('\nExercicio 5 (Floyd-Warshall):\n')
		graph_path = "./instances/caminho_minimo/fln_pequena.net"
		graph = buildGraphFromFile(graph_path)
		print(floydWarshall(graph))

if __name__ == "__main__":
	main()