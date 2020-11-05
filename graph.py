from vertex import Vertex

class NotDirectedGraph:
	def __init__(self):
		self.vertices = dict()
		self.graph = dict()
		self.numberOfEdges = 0

	def addVertex(self, vertex_id: str, vertex_name: str) -> None:
		if not self.hasVertexId(vertex_id):
			self.vertices[vertex_id] = vertex_name
			self.graph[vertex_id] = Vertex(vertex_id, vertex_name)

	def addEdge(self, vertex1_id: str, vertex2_id: str, weight: float) -> None:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].addEdge(vertex2_id, weight)
			if vertex1_id != vertex2_id:
				self.graph[vertex2_id].addEdge(vertex1_id, weight)
			self.numberOfEdges += 1
		else:
			self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def removeEdge(self, vertex1_id: str, vertex2_id: str) -> None:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].removeEdge(vertex2_id)
			if vertex1_id != vertex2_id:
				self.graph[vertex2_id].removeEdge(vertex1_id)
			self.numberOfEdges -= 1
		else:
			self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	# qtdVertices() -> O(1) (len(object) is O(1): https://stackoverflow.com/q/1115313) 
	def getNumberOfVertices(self) -> int: 
		return len(self.vertices)

	# qtdArestas() -> O(1) (only costs the time to access self.numberOfEdges)
	def getNumberOfEdges(self) -> int: 
		return self.numberOfEdges

	# grau(v) -> O(1) (hasVertexId = O(1), self.graph[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item)), self.graph[vertex_id].degree = O(1))
	def getVertexDegree(self, vertex_id: str) -> int:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].degree

		self.__rise_exception_invalid_ids(vertex_id)

	# rotulo(v) -> O(1) (hasVertexId = O(1), self.graph[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item)), self.graph[vertex_id].vertex_name = O(1))
	def getVertexLabel(self, vertex_id: str) -> int:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].vertex_name

		self.__rise_exception_invalid_ids(vertex_id)

	# vizinhos(v) -> O(1) (hasVertexId = O(1), self.graph[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item)), self.graph[vertex_id].neighbors = O(1))
	def getVertexNeighbors(self, vertex_id: str) -> set:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].neighbors

		self.__rise_exception_invalid_ids(vertex_id)

	# O(1) -> https://wiki.python.org/moin/TimeComplexity/#dict (k in d), "in" operation is O(1)
	def hasVertexId(self, vertex_id: str) -> bool:
		return vertex_id in self.vertices

	# haAresta(u, v) -> O(1) (hasVertexId = O(1), self.graph[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item)), self.graph[vertex1_id].hasEdgeTo(vertex2_id) = O(1))
	def hasEdge(self, vertex1_id: str, vertex2_id: str) -> bool:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].hasEdgeTo(vertex2_id)

		self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	# peso(u, v) -> O(1) (hasVertexId = O(1), self.graph[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item)), self.graph[vertex1_id].getEdgeWeight(vertex2_id) = O(1))
	def weight(self, vertex1_id: str, vertex2_id: str) -> float:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].getEdgeWeight(vertex2_id)

		self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def __rise_exception_invalid_ids(self, *vertices_ids) -> None:
		not_included_ids = set()
		for vertex_id in vertices_ids:
			if not self.hasVertexId(vertex_id):
				not_included_ids.add(vertex_id)

		raise Exception("ids \""+str(not_included_ids)+"\" aren't in your vertices")

	def copy(self):
		graph_copy = NotDirectedGraph()
		graph_copy.vertices = self.vertices.copy()
		for vertex_id in self.graph:
			graph_copy.graph[vertex_id] = self.graph[vertex_id].copy()
		graph_copy.numberOfEdges = self.numberOfEdges
		return graph_copy


