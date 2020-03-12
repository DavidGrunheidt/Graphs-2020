class Vertex:
	def __init__(self, vertex_name):
		self.vertex = vertex_name
		self.neighbors = set()
		self.edges = dict()
		self.degree = 0

	def addEdge(self, destiny_vertex: str, weight: int) -> None:
		if (destiny_vertex not in self.neighbors):
			self.neighbors.add(destiny_vertex)
			self.edges[destiny_vertex] = [weight] 
		else:
			self.edges[destiny_vertex].append(weight)

		if (destiny_vertex == self.vertex):
			self.degree += 2
		else:
			self.degree += 1

	def hasEdgeTo(self, destiny_vertex: str) -> bool:
		return destiny_vertex in self.neighbors

	def getEdgeWeight(self, destiny_vertex: str) -> bool:
		if self.hasEdgeTo(destiny_vertex):
			return self.edges[destiny_vertex]
		else: 
			return sys.intmax

class NotDirectedGraph:
	def __init__(self, vertices: set):
		self.vertices = vertices
		self.graph = dict()
		self.numberOfEdges = 0
		
		for vertex_name in vertices:
			self.graph[vertex_name] = Vertex(vertex_name)

	def addVertex(self, vertex_name: str) -> None:
		if not self.hasVertex(vertex_name):
			self.vertices.add(vertex_name)
			self.graph[vertex_name] = Vertex(vertex_name)

	def addEdge(self, origin_vertex: str, destiny_vertex: str, weight: float) -> None:	
		if self.hasVertex(origin_vertex) and self.hasVertex(destiny_vertex):
			self.graph[destiny_vertex].addEdge(origin_vertex, weight)
			self.graph[origin_vertex].addEdge(destiny_vertex, weight)
			self.numberOfEdges += 1
		else:
			if not self.hasVertex(origin_vertex):
				print(origin_vertex + " is not in your vertices: " + ','.join(self.vertices) + "\n")
			if not self.hasVertex(destiny_vertex):
				print(destiny_vertex + " is not in your vertices: " + ','.join(self.vertices) + "\n")

	def getNumberOfVertices(self) -> int: 
		return len(self.vertices)

	def getNumberOfEdges(self) -> int: 
		return self.numberOfEdges

	def getVertexDegree(self, vertex_name: str) -> int:
		if self.hasVertex(vertex_name):
			return self.graph[vertex_name].degree
		else:
			print(vertex_name + " is not in your vertices list: " + ','.join(self.vertices))
			return -1

	def getVertexNeighbours(self, vertex_name) -> set:
		if self.hasVertex(vertex_name):
			return self.graph[vertex_name].neighbors
		else: 
			print(vertex_name + " is not in your vertices: " + ','.join(self.vertices))

	def hasVertex(self, vertex_name: str) -> bool:
		return vertex_name in self.vertices

	def hasEdge(self, vertex1: str, vertex2: str) -> bool:
		if self.hasVertex(vertex1) and self.hasVertex(vertex2):
			return self.graph[vertex1].hasEdgeTo(vertex2)
		else:
			return False

	def weight(self, vertex1: str, vertex2: str) -> bool:
		if self.hasVertex(vertex1) and self.hasVertex(vertex2):
			return self.graph[vertex1].getEdgeWeight(vertex2)
		else:
			return sys.maxint

graph = NotDirectedGraph({"a", "b", "c", "d"})

graph.addEdge("a", "b", 20)
graph.addEdge("a", "c", 30)
graph.addEdge("a", "d", 40)
graph.addEdge("c", "d", 25)
graph.addEdge("c", "b", 25)

print(graph.getVertexDegree("a"))
print(graph.getVertexDegree("b"))
print(graph.getVertexDegree("c"))
print(graph.getNumberOfEdges())
print(graph.getNumberOfVertices())