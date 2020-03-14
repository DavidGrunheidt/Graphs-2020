import os
from graph import NotDirectedGraph

def buildGraphFromFile(file_path: str) -> 'Graph':
	graph_file = open(file_path, 'r')

	graph = NotDirectedGraph()

	line = graph_file.readline() #ignoring first line

	build_vertices = True
	for line in graph_file:
		line = line.rstrip("\n\r").rstrip(' ') #remove new line character and spaces in the end of the line

		if build_vertices:
			if line in {"*edges"}:
				build_vertices = False
			else:
				try:
					splittedLine = line.split(' ', 1)

					if (len(splittedLine) == 2):
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

def breadthFirstSearch(graph: 'Graph') -> str:
	pass