import os
import sys
import random
from graphsManager import *

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

	randVertexId = random.choice(list(graph.vertices.keys()))
	randVertexName = graph.getVertexLabel(randVertexId)
	randVertexNeighbors = graph.getVertexNeighbors(randVertexId)
	randVertexRandNeighbor = random.choice(list(randVertexNeighbors))
	otherRandVertexId0 = random.choice(list(graph.vertices.keys()))
	otherRandVertexId1 = random.choice(list(graph.vertices.keys()))

	print('Number of vertices = ' + str(graph.getNumberOfVertices()))
	print('Number of edges = ' + str(graph.getNumberOfEdges()))
	print('Vertex ' + randVertexId + ' degree = ' + str(graph.getVertexDegree(randVertexId)))
	print('Vertex ' + randVertexId + ' name = ' + randVertexName)
	print('Vertex ' + randVertexId + ' neighbors = ' + str(randVertexNeighbors))
	print('Vertex ' + randVertexId + ' has edge with ' + randVertexRandNeighbor + ' = ' + str(graph.hasEdge(randVertexId, randVertexRandNeighbor)))
	print('Vertex ' + randVertexId + ' has edge with ' + otherRandVertexId0 + ' = ' + str(graph.hasEdge(randVertexId, otherRandVertexId0)))
	print('Vertex ' + randVertexId + ' has edge with ' + otherRandVertexId1 + ' = ' + str(graph.hasEdge(randVertexId, otherRandVertexId1)))
	print('Edge ' + randVertexId + ' <-> ' + randVertexRandNeighbor + ' weight(s) = ' + str(graph.weight(randVertexId, randVertexRandNeighbor)))

	print('\nEnd of tests for ' + path)
	print('---------------------------------------------')

def main():

	maybePath = sys.argv[len(sys.argv)-1]

	if maybePath == "testAll":
		graphs = buildEachInstance("instances")

		for graph in graphs:
			if len(graphs[graph].vertices) == 0:
				print("Graph in " + graph + ' has a problem')
				return

		print("Nothing wrong with the inputs.\nStarting tests...\n")

		for graph in graphs:
			test_graph(graph, graphs[graph])
	else:
		graph_path = "./instances/ciclo_euleriano/ContemCicloEuleriano.net"
		graph = buildGraphFromFile(graph_path)
		# test_graph(graph_path, graph)
		print(breadthFirstSearch(graph, '1'))

if __name__ == "__main__":
	main()