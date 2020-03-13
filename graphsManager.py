from graph import NotDirectedGraph

def buildGraphFromFile(file_path: str) -> 'Graph':
	graph_file = open(file_path, 'r')

	graph = NotDirectedGraph()

	line = graph_file.readline() #ignoring first line

	build_vertices = True
	for line in graph_file:
		line = line.rstrip("\n\r") #remove new line character

		if build_vertices:
			if line == "*edges":
				build_vertices = False
			else:
				try:
					splittedLine = line.split(' ', 1)

					vertexId = int(splittedLine[0])
					vertexName = splittedLine[1].replace("\"", "")

					graph.addVertex(vertexId, vertexName)
				except ValueError:
					print("Error while adding vertex: Vertex id \""+splittedLine[0]+"\" isn't an int (must be)")
					return NotDirectedGraph()
		else:
			try:
				splittedLine = line.split(' ')

				if len(splittedLine) == 3:
					origin_vertex_id = int(splittedLine[0])
					destiny_vertex_id = int(splittedLine[1])
					edge_weight = float(splittedLine[2])

					graph.addEdge(origin_vertex_id, destiny_vertex_id, edge_weight)
				else:
					raise Exception("Error while building edge: \""+line+"\" isn't in the default template: (id id weight)")
			except ValueError:
				print("Error while building edge: \""+splittedLine[0]+"\" isn't an int or \""+splittedLine[1]+"\" isn't an int or \""+splittedLine[2]+"\" isn't a float")
				return NotDirectedGraph()
			except Exception as error:
				print(error)
				return NotDirectedGraph()

	return graph