import os
from graph import NotDirectedGraph

# ler(arquivo)
def buildGraphFromFile(file_path: str) -> 'Graph':
	graph_file = open(file_path, 'r')

	graph = NotDirectedGraph()

	graph_file.readline() #ignoring first line

	build_vertices = True
	for line in graph_file:
		line = line.rstrip("\n\r").rstrip(' ') #remove new line character and spaces in the end of the line

		if build_vertices:
			if line in {"*edges"}:
				build_vertices = False
			else:
				try:
					splittedLine = line.split(' ', 1)

					if len(splittedLine) == 2:
						vertexId = splittedLine[0]
						vertexName = splittedLine[1].replace("\"", "")

						graph.addVertex(vertexId, vertexName)
					else:
						raise Exception("Error while building vertex (graph = "+file_path+"): \""+line+"\" isn't in the default template: (id label)")

				except Exception as error:
					print("(graph = "+file_path+"):"+str(error))
					return NotDirectedGraph()
		else:
			try:
				splittedLine = line.split(' ')

				if len(splittedLine) == 3:
					origin_vertex_id = splittedLine[0]
					destiny_vertex_id = splittedLine[1]
					edge_weight = float(splittedLine[2])

					graph.addEdge(origin_vertex_id, destiny_vertex_id, edge_weight)
				else:
					raise Exception("Error while building edge (graph = "+file_path+"): \""+line+"\" isn't in the default template: (id id weight)")
			except ValueError:
				print("Error while building edge (graph = "+file_path+"): \""+splittedLine[2]+"\" (your weight) isn't a float")
				return NotDirectedGraph()
			except Exception as error:
				print("(graph = "+file_path+"): "+str(error))
				return NotDirectedGraph()

	return graph

def breadthFirstSearch(graph: NotDirectedGraph, inital_vertex_id: str) -> str:
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

	return search